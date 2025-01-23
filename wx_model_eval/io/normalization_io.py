"""Miscellaneous helper methods."""

import xarray
from wx_model_eval.outside_code import error_checking

FIELD_DIM = 'field_name'
QUANTILE_LEVEL_DIM = 'quantile_level'

MEAN_VALUE_KEY = 'mean_value'
MEAN_SQUARED_VALUE_KEY = 'mean_squared_value'
STDEV_KEY = 'standard_deviation'
QUANTILE_KEY = 'quantile'


def read_normalization_file(netcdf_file_name):
    """Reads normalization parameters for target fields from NetCDF file.

    :param netcdf_file_name: Path to input file.
    :return: norm_param_table_xarray: xarray table (metadata and variable names
        should make the table self-explanatory).
    """

    error_checking.assert_file_exists(netcdf_file_name)
    return xarray.open_dataset(netcdf_file_name)\
