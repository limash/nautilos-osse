from dataclasses import dataclass

@dataclass
class ArgumentsSpring2017:
    start_time: str = '2017-02-01'
    end_time: str = '2017-02-07'
    input_grid_file: str = '/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc'
    roho800orig_files: tuple = (
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0525.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0526.nc',
    )
    roho800_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0003.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0004.nc',
    )
    roho160_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0002.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0003.nc',
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
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0055.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0056.nc',
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
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0107.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/2_2017_01_15-2019_12_27_v2bn/his_0108.nc',
    )
    roho160_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0075.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_his_0076.nc',
    )
    stations: str = '/cluster/projects/nn9297k/shmiak/roho160_data/1_2017-01-15_to_2019-07-16/roho160_sta.nc'
    wc13_obs_file: str = '/cluster/home/shmiak/src/roms-applications/WC13/Data/wc13_obs.nc'
    output_obs_file: \
        str = '/cluster/projects/nn9297k/shmiak/roho800_data/input_data/obs_i4dvar_4st_temp_2019-02-01_to_2019-02-07.nc'
