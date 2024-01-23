"""
Runs a roms model (romsM) sequentially
using phys data from another roms output (PHYSPATH)
and biogeo data from the previous step of the current run
It need `FILES` to be in the same folder
"""
import os
import glob
import shutil
import subprocess
from datetime import timedelta

import cftime
import numpy as np
import xarray as xr

VARINFO = "varinfo.dat"
ROHO800IN = "roho800.in"
STATIONS = "stations.in"
FABM = "fabm.yaml"
RFABM = "rfabm.in"
EXEC = "romsM"

FILES = (
    VARINFO, ROHO800IN, STATIONS, FABM, RFABM, EXEC
)

YEAR2017PATH = "/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_avg/roho800_avg_0131.nc"
TIME2017 = (2017, 1, 15)
DAYS_1948_2017 = 25217
YEAR2018PATH = "/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_avg/roho800_avg_0144.nc"
TIME2018 = (2018, 1, 15)
DAYS_1948_2018 = 25582
YEAR2019PATH = "/cluster/projects/nn9490k/ROHO800/STORAGE/ROHO800_hindcast_2007_2019_v2bn/roho800_v2bn_avg/roho800_avg_0157.nc"
TIME2019 = (2019, 1, 15)
DAYS_1948_2019 = 25947

PHYSPATH = "/cluster/projects/nn9297k/shmiak/roho800_data/output_data/forward/3_2017_01_15-2019_12_27"

VARS_TO_UPDATE = (
    "AKs", "AKt", "AKv",
    "rho", "salt", "temp",
    "u", "ubar", "v", "vbar", "w", "zeta"
)


def create_and_copy(directory_path, files_to_copy):
    # Check if the directory exists, create it if not
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        # If the directory exists, delete its contents
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        print(f"Contents of directory '{directory_path}' deleted.")

    # Copy files to the destination directory
    for file_to_copy in files_to_copy:
        destination_path = os.path.join(directory_path, file_to_copy)
        shutil.copy(file_to_copy, destination_path)
        print(f"File '{file_to_copy}' copied to '{destination_path}'.")


def create_first_init(directory_path, roms_file_path, time_cftime, time_isel=-1):
    """
    opens ROMS output nc file, assigns new time coordinate,
    saves to a new file and returns its name
    """
    ds_init = xr.open_dataset(roms_file_path)
    ds_init = ds_init.isel(ocean_time=time_isel)
    ds_init = ds_init.assign_coords(ocean_time=[time_cftime])
    file_name = os.path.join(directory_path, f"init_{time_cftime.strftime(format='%d-%m-%Y')}.nc")
    ds_init.to_netcdf(
        file_name,
        encoding={
            'ocean_time':{'units': "days since 1948-01-01"},
            }
        )
    return file_name


def create_init(directory_path, roms_file_path, time_cftime, dir_phys):
    """
    A generator, which extracts VARS_TO_UPDATE variables from ROMS phys file
    (another ROMS model output, better resolution for example)
    and update the previous ROMS output to create a new ROMS init file.
    Returns a destination of the created init file.

    directory_path: a directory where to save time_cftime init file
    roms_file_path: the last ROMS output from the previous run, with biogeo vars
    time_cftime: init file start time
    dir_phys: the roms800 (da version) output
    """

    files_phys = iter(sorted(glob.glob(f"{dir_phys}/his_*.nc")))
    file_phys = next(files_phys)
    while True:
        ds_phys = xr.open_dataset(file_phys)
        try:
            ds_phys = ds_phys.sel(ocean_time=np.datetime64(time_cftime))
        except KeyError:
            file_phys = next(files_phys)
            continue

        ds_init = xr.open_dataset(roms_file_path)
        ds_init = ds_init.isel(ocean_time=-1)  # should match time_cftime, slice?
        assert ds_init.ocean_time.values == np.datetime64(time_cftime)
        ds_init = ds_init.assign_coords(ocean_time=[time_cftime])  # to make 1d dim

        for variable in VARS_TO_UPDATE:
            ds_init[variable] = ds_phys[variable]

        file_name = os.path.join(directory_path, f"init_{time_cftime.strftime(format='%d-%m-%Y')}.nc")
        ds_init.to_netcdf(
            file_name,
            encoding={
                'ocean_time':{'units': "days since 1948-01-01"},
                }
            )

        received = yield file_name
        directory_path, roms_file_path, time_cftime = received


def change_the_line(file_path, start_symbols, new_line_to_replace):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line starting with `start_symbols`
    index_to_replace = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith(start_symbols):
            index_to_replace = i
            break

    # If the line is found, replace it with another line
    if index_to_replace is not None:
        lines[index_to_replace] = new_line_to_replace

        # Write the updated contents back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Line replaced successfully.")
    else:
        print(f"Line starting with {start_symbols} not found.")


def run_roms(directory_path):
    executable = os.path.join(directory_path, EXEC)
    config = os.path.join(directory_path, ROHO800IN)
    output = os.path.join(directory_path, "output.log")
    command = f"time mpirun {executable} {config} > {output}"
    process = subprocess.Popen(command, cwd=directory_path, shell=True)
    process.communicate()


def main(init_time_tuple, init_av_file_path, days_since_1948):
    # Stage 1: run ROMS from roho800original average output
    #
    # 1. create a folder for the first run, copy files to it :
    directory_path = os.path.join(os.getcwd(), "0_iter")
    create_and_copy(directory_path, FILES)

    # 2. create the first init file from the Phils v2bn run
    time_cftime = cftime.datetime(*init_time_tuple)
    init_name = create_first_init(directory_path, init_av_file_path, time_cftime, time_isel=1)

    # 3. modify roms ININAME in roho800.in
    change_the_line(
        os.path.join(directory_path, ROHO800IN),
        "ININAME ==",
        f"ININAME == {init_name}\n"
    )

    # 4. modify roms DSTART in roho800.in
    change_the_line(
        os.path.join(directory_path, ROHO800IN),
        "DSTART =",
        f"DSTART = {days_since_1948}\n"
    )

    run_roms(directory_path)

    # Stage 2: generator creation

    prev_dir_path = directory_path

    directory_path = os.path.join(os.getcwd(), "1_iter")
    create_and_copy(directory_path, FILES)

    time_cftime = time_cftime + timedelta(days=3)
    prev_roms_output = os.path.join(prev_dir_path, "roho800_his_0001.nc")

    create_init_gen = create_init(directory_path, prev_roms_output, time_cftime, PHYSPATH)
    init_name = next(create_init_gen)

    change_the_line(
        os.path.join(directory_path, ROHO800IN),
        "ININAME ==",
        f"ININAME == {init_name}\n"
    )

    days_since_1948 += 3
    change_the_line(
        os.path.join(directory_path, ROHO800IN),
        "DSTART =",
        f"DSTART = {days_since_1948}\n"
    )

    run_roms(directory_path)

    # Stage 3: stepping
    for i in range(2, 50):
        prev_dir_path = directory_path

        directory_path = os.path.join(os.getcwd(), f"{i}_iter")
        create_and_copy(directory_path, FILES)

        time_cftime = time_cftime + timedelta(days=3)
        prev_roms_output = os.path.join(prev_dir_path, "roho800_his_0001.nc")

        init_name = create_init_gen.send((directory_path, prev_roms_output, time_cftime))

        change_the_line(
            os.path.join(directory_path, ROHO800IN),
            "ININAME ==",
            f"ININAME == {init_name}\n"
        )

        days_since_1948 += 3
        change_the_line(
            os.path.join(directory_path, ROHO800IN),
            "DSTART =",
            f"DSTART = {days_since_1948}\n"
        )

        run_roms(directory_path)


if __name__ == "__main__":
    main(TIME2019, YEAR2019PATH, DAYS_1948_2019)
