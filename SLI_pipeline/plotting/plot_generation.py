from pathlib import Path
import logging
import warnings
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
from conf.global_settings import OUTPUT_DIR

warnings.filterwarnings("ignore")


def generate_plots():
    '''
    Generates sanity check plots for each indicator and GMSL
    '''
    ind_path = OUTPUT_DIR / 'indicator/indicators.nc'
    vars = ['enso_index', 'pdo_index', 'iod_index', 'spatial_mean']
    ds = xr.open_dataset(ind_path)
    end_time = ds.time.values[-1]
    start_time = end_time - np.timedelta64(365*5, 'D')
    pdo_start_time = end_time - np.timedelta64(365*10, 'D')
    spatial_start_time = end_time - np.timedelta64(365*7, 'D')

    slice_start = None

    output_path = OUTPUT_DIR / 'indicator/plots'
    output_path.mkdir(parents=True, exist_ok=True)

    for var in vars:

        if 'pdo' in var:
            var_ds = ds[var].sel(time=slice(pdo_start_time, end_time))
        elif 'spatial' in var:
            var_ds = ds[var].sel(time=slice(spatial_start_time, end_time))
            var_ds.values = var_ds.values * 100
            var_ds.attrs['units'] = 'cm'
        else:
            var_ds = ds[var].sel(time=slice(start_time, end_time))

        plt.rcParams.update({'font.size': 16})
        plt.figure(figsize=(10, 5))
        
        var_ds.plot.line(lw=3)
        
        plt.grid()
        plt.title(var)
        plt.savefig(f'{output_path}/{var}.png', dpi=150)
        plt.cla()
