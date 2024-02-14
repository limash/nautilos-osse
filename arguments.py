import re
import glob
from dataclasses import dataclass

def natural_sort(l):  # noqa: E741
    convert = lambda text: int(text) if text.isdigit() else text.lower()  # noqa: E731
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]  # noqa: E731
    return sorted(l, key=alphanum_key)


@dataclass
class ArgumentsSpring2017:
    start_time: str = '2017-02-01'
    end_time: str = '2017-04-01'
    input_grid_file: str = '/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc'
    roho800orig_files: tuple = tuple(
        natural_sort(
            glob.glob('/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_05*.nc')
        )
    )
    roho800_files: tuple = tuple(
        natural_sort(
            glob.glob('/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_000*.nc')
        )
    )
    roho160_files: tuple = tuple(
        natural_sort(
            glob.glob('/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/roho160_his_00*.nc')
        )
    )
    baseline_files: tuple = tuple(
        natural_sort(
            glob.glob('/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/*_iter/roho800_his_0001.nc')
        )
    )
    nature_files: tuple = tuple(
        natural_sort(
            glob.glob('/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/*_iter/roho800_his_0001.nc')
        )
    )
    stations: str = '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_sta.nc'
    wc13_obs_file: str = '/cluster/home/shmiak/src/roms-applications/WC13/Data/wc13_obs.nc'
    output_obs_file: \
        str = '/cluster/projects/nn9297k/shmiak/roho800_data/input_data/obs_i4dvar_4st_temp_2017-02-01_to_2017-02-07.nc'

@dataclass
class ArgumentsSpring2018:
    start_time: str = '2018-02-01'
    end_time: str = '2018-02-07'
    input_grid_file: str = '/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc'
    roho800orig_files: tuple = (
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0577.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0578.nc',
    )
    roho800_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0055.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0056.nc',
    )
    roho160_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0039.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0040.nc',
    )
    stations: str = '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_sta.nc'
    wc13_obs_file: str = '/cluster/home/shmiak/src/roms-applications/WC13/Data/wc13_obs.nc'
    output_obs_file: \
        str = '/cluster/projects/nn9297k/shmiak/roho800_data/input_data/obs_i4dvar_4st_temp_2018-02-01_to_2018-02-07.nc'

@dataclass
class ArgumentsSpring2019:
    start_time: str = '2019-02-01'
    end_time: str = '2019-02-07'
    input_grid_file: str = '/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc'
    roho800orig_files: tuple = (
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0629.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0630.nc',
    )
    roho800_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0107.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0108.nc',
    )
    roho160_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0075.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0076.nc',
    )
    stations: str = '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_sta.nc'
    wc13_obs_file: str = '/cluster/home/shmiak/src/roms-applications/WC13/Data/wc13_obs.nc'
    output_obs_file: \
        str = '/cluster/projects/nn9297k/shmiak/roho800_data/input_data/obs_i4dvar_4st_temp_2019-02-01_to_2019-02-07.nc'
