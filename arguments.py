from dataclasses import dataclass

@dataclass
class ArgumentsSpring2017:
    start_time: str = '2017-02-01'
    end_time: str = '2017-04-01'
    input_grid_file: str = '/cluster/projects/nn9490k/ROHO800/Grid/ROHO800_grid_fix5.nc'
    roho800orig_files: tuple = (
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0525.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0526.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0527.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0528.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0529.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0530.nc',
        '/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_his/roho800_his_0531.nc',
    )
    roho800_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0003.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27/his_0004.nc',
    )
    roho160_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/roho160_his_002.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/roho160_his_003.nc',
        '/cluster/projects/nn9297k/shmiak/roho160_data/3_2017-01-15_to_2019-07-16_with_AKx_no_lakes/roho160_his_004.nc',
    )
    baseline_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/5_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/6_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/7_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/8_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/9_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/10_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/11_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/12_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/13_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/14_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/15_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/16_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/17_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/18_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/19_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/20_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/21_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/22_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/23_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/24_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/25_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/26_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/27_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/28_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_forward/y2017/29_iter/roho800_his_0001.nc',
    )
    nature_files: tuple = (
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/17_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/18_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/19_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/20_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/21_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/22_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/23_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/24_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/25_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/26_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/27_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/28_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/29_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/30_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/31_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/32_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/33_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/34_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/35_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/36_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/37_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/38_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/39_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/40_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/41_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/42_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/43_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/44_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/45_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/46_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/47_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/48_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/49_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/50_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/51_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/52_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/53_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/54_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/55_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/56_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/57_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/58_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/59_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/60_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/61_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/62_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/63_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/64_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/65_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/66_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/67_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/68_iter/roho800_his_0001.nc',
        '/cluster/projects/nn9297k/shmiak/roho800_data/output_data/orig_with_phys_from_roho160/2017_3_months/69_iter/roho800_his_0001.nc',
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
