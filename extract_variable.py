"""
Extracts a variable from several netcdf files.
"""
import os

import xarray as xr

from arguments import (
    ArgumentsSpring2017,  # noqa: F401
)


def write_variables(var_names: tuple, dir_name: str, ds):
    for var_name in var_names:
        print(f"Start: {var_name}")
        ds[var_name].to_netcdf(dir_name + f'/{var_name}.nc', 'w')
        print(f"Finish: {var_name}")
    ds.close()


def main():
    variables = ('rho', 'temp', 'salt', 'u', 'v', 'AKs', 'AKt', 'AKv', 'P1_Chl', 'zeta')
    args = ArgumentsSpring2017()
    file_names = args.nature_files

    time_slice = slice(args.start_time, args.end_time)
    directory_path = os.path.dirname(os.path.dirname(file_names[0]))
    ds = xr.open_mfdataset(file_names).sel(ocean_time=time_slice)

    write_variables(variables, directory_path, ds)


if __name__ == "__main__":
    main()
