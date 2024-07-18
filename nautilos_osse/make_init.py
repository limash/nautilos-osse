import os

import cftime
import xarray as xr

YEAR2017PATH = "/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_avg/roho800_avg_0132.nc"
TIME2017 = (2017, 2, 1)
DIRPATH = "/cluster/projects/nn9297k/shmiak/roho800_data/input_data"


def create_first_init(directory_path, roms_file_path, time_cftime, time_isel=-1):
    """
    opens ROMS output nc file, assigns new time coordinate,
    saves to a new file and returns its name
    time units different from the version in run_sequence,
    the second ROMS NLM run accepts only seconds since time reference
    """
    ds_init = xr.open_dataset(roms_file_path)
    ds_init = ds_init.isel(ocean_time=time_isel)
    ds_init = ds_init.assign_coords(ocean_time=[time_cftime])
    file_name = os.path.join(directory_path, f"init_{time_cftime.strftime(format='%d-%m-%Y')}.nc")
    ds_init.to_netcdf(
        file_name,
        encoding={
            'ocean_time':{'units': "seconds since 1948-01-01"},
            }
        )
    return file_name


def main(init_time_tuple, init_av_file_path, directory_path):

    time_cftime = cftime.datetime(*init_time_tuple)
    init_name = create_first_init(directory_path, init_av_file_path, time_cftime, time_isel=0)
    print(f"File name {init_name} created.")


if __name__ == "__main__":
    main(TIME2017, YEAR2017PATH, DIRPATH)
