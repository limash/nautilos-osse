"""
It regrids roho160 output to the roho800 domain (f function).
roho800 domain is larger, so it extrapolates towards the boundaries.
Also erases lakes from the roms output (g function)
To run the interactive job (FRAM):
`salloc --nodes=1 --time=02:00:00 --qos=short --account=nn9297k`
"""

import re
import glob
import itertools
from multiprocessing import Pool
from dataclasses import dataclass

import numpy as np
import xarray as xr
import xesmf as xe


@dataclass
class RomsVariable:
    name: str
    lon_name: str
    lat_name: str
    eta_name: str
    xi_name: str
    mask_name: str
    s_name: str


def regrid(ds_grid, ds_data, parameter_name, lon_name, lat_name):
    ds_grid = ds_grid.rename({lon_name: "lon", lat_name: "lat"})
    ds_data = ds_data.rename({lon_name: "lon", lat_name: "lat"})
    regridder = xe.Regridder(ds_data, ds_grid, 'bilinear', unmapped_to_nan=True)
    return regridder(ds_data[parameter_name])


def fit_grid(ds_grid, da, eta_name, xi_name, mask_name):
    da = da.interpolate_na(dim=eta_name, method="nearest", fill_value="extrapolate")
    da = da.interpolate_na(dim=xi_name, method="nearest", fill_value="extrapolate")
    return ds_grid[mask_name] * da


def fill_variables():
    variables = []
    variables.append(RomsVariable("temp", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_rho"))
    variables.append(RomsVariable("salt", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_rho"))
    variables.append(RomsVariable("u", "lon_u", "lat_u", "eta_u", "xi_u", "mask_u", "s_rho"))
    variables.append(RomsVariable("ubar", "lon_u", "lat_u", "eta_u", "xi_u", "mask_u", None))
    variables.append(RomsVariable("v", "lon_v", "lat_v", "eta_v", "xi_v", "mask_v", "s_rho"))
    variables.append(RomsVariable("vbar", "lon_v", "lat_v", "eta_v", "xi_v", "mask_v", None))
    variables.append(RomsVariable("zeta", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", None))
    variables.append(RomsVariable("w", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_w"))
    variables.append(RomsVariable("AKs", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_w"))
    variables.append(RomsVariable("AKt", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_w"))
    variables.append(RomsVariable("AKv", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_w"))
    variables.append(RomsVariable("rho", "lon_rho", "lat_rho", "eta_rho", "xi_rho", "mask_rho", "s_rho"))
    return variables


def regrid_fit(ds_grid, ds_data, roms_variable):
    """
    Finds a roms_variable in ds_data and then
    regrids and interpolates + extrapolates it to lats and lons from ds_grid
    """
    da = regrid(ds_grid,
                ds_data,
                roms_variable.name,
                roms_variable.lon_name,
                roms_variable.lat_name
                )
    return fit_grid(ds_grid,
                    da,
                    roms_variable.eta_name,
                    roms_variable.xi_name,
                    roms_variable.mask_name
                    )


def get_slices(steps: int, num: int):
    samples = np.linspace(0, steps, num).astype(int)  # astype int rounds down
    return itertools.pairwise(samples)


def f(ds_grid, file_names):
    """
    Regridding
    """
    roms_variables = fill_variables()
    pattern = re.compile(r'\d+')
    for file_name in file_names:
        matches = pattern.findall(file_name)
        numbers = [int(match) for match in matches]
        i = numbers[-1]

        ds_data = xr.open_dataset(file_name)
        ds_dict = {}
        for var in roms_variables:
            da = regrid_fit(ds_grid, ds_data, var)
            try:
                da = da.transpose("ocean_time", var.s_name, var.eta_name, var.xi_name)
                ds_dict[var.name] = (["ocean_time", var.s_name, var.eta_name, var.xi_name], da.values)
            except ValueError:
                da = da.transpose("ocean_time", var.eta_name, var.xi_name)
                ds_dict[var.name] = (["ocean_time", var.eta_name, var.xi_name], da.values)
        xr.Dataset(
            data_vars=ds_dict,
            coords=dict(
                ocean_time=ds_data.ocean_time.values,
            ),
        ).to_netcdf(
            f'/cluster/projects/nn9297k/shmiak/roho800_data/interpolated_from_roho160_phys/his_{i:03d}_from_roho160.nc'
        )
        print(f"File {i:03d}_from_roho160.nc saved")


def g(ds_grid, file_names):
    """
    Lakes erasing, it uses a new grid without lakes to update the data;
    also it takes data only at the midnight
    """
    roms_variables = fill_variables()
    pattern = re.compile(r'\d+')
    for file_name in file_names:
        matches = pattern.findall(file_name)
        numbers = [int(match) for match in matches]
        i = numbers[-1]

        ds_data = xr.open_dataset(file_name)
        ds_data = ds_data.sel(ocean_time=ds_data['ocean_time'].dt.hour == 0)
        ds_dict = {}
        for var in roms_variables:
            da =  ds_data[var.name] / ds_grid[var.mask_name].astype(np.float32)
            print(f"Variable {var.name} processed.")
            da.values[np.isinf(da.values)] = np.nan
            try:
                da = da.transpose("ocean_time", var.s_name, var.eta_name, var.xi_name)
                ds_dict[var.name] = (["ocean_time", var.s_name, var.eta_name, var.xi_name], da.values)
            except ValueError:
                da = da.transpose("ocean_time", var.eta_name, var.xi_name)
                ds_dict[var.name] = (["ocean_time", var.eta_name, var.xi_name], da.values)
        xr.Dataset(
            data_vars=ds_dict,
            coords=dict(
                s_rho=(["s_rho"], ds_data.s_rho.values),
                s_w=(["s_w"], ds_data.s_w.values),
                ocean_time=(["ocean_time"], ds_data.ocean_time.values),
                lon_rho=(["eta_rho", "xi_rho"], ds_data.lon_rho.values),
                lat_rho=(["eta_rho", "xi_rho"], ds_data.lat_rho.values),
                lon_u=(["eta_u", "xi_u"], ds_data.lon_u.values),
                lat_u=(["eta_u", "xi_u"], ds_data.lat_u.values),
                lon_v=(["eta_v", "xi_v"], ds_data.lon_v.values),
                lat_v=(["eta_v", "xi_v"], ds_data.lat_v.values),
                lon_psi=(["eta_psi", "xi_psi"], ds_data.lon_psi.values),
                lat_psi=(["eta_psi", "xi_psi"], ds_data.lat_psi.values),
            ),
        ).to_netcdf(
            f'/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/roho160_his_{i:03d}.nc'
        )
        print(f"File roho160_his_{i:03d}.nc saved")


def split_list(input_list, num_splits):
    # Calculate the length of each sub-list
    sublist_length = len(input_list) // num_splits

    # Split the list into sub-lists
    split_lists = [input_list[i * sublist_length: (i + 1) * sublist_length] for i in range(num_splits)]

    return split_lists


if __name__ == "__main__":
    # num splits defines the number of processes
    num_splits = 2

    # memory limit: 2 processes max
    file_names = sorted(glob.glob(
        "/cluster/projects/nn9297k/shmiak/roho160_data/2_2017-01-15_to_2019-07-16_with_AKx/*his*.nc"
    ))[:10]

    # memory limit: 5 processes max
    # file_names = sorted(glob.glob(
    #     "/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/*his*.nc"
    # ))[:10]

    file_names_splits = split_list(file_names, num_splits)

    def wrapper_erase_lakes(x):
        ds_grid = xr.open_dataset("/cluster/projects/nn9297k/ROHO160+/InputData/Grid/roho_160m_sigma3_min20_no_lakes.nc")
        g(ds_grid, x)

    def wrapper_regrid(x):
        ds_grid = xr.open_dataset('/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc')
        f(ds_grid, x)

    # lambda cannot be pickled (python3.10)
    with Pool(processes=num_splits) as p:
        p.map(wrapper_erase_lakes, file_names_splits)
