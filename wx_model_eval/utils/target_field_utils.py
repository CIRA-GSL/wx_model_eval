"""Helper methods for understanding properties of each target variable."""

from wx_model_eval.outside_code import error_checking

TEMPERATURE_2METRE_NAME = 'temperature_2m_agl_kelvins'
DEWPOINT_2METRE_NAME = 'dewpoint_2m_agl_kelvins'
U_WIND_10METRE_NAME = 'u_wind_10m_agl_m_s01'
V_WIND_10METRE_NAME = 'v_wind_10m_agl_m_s01'
WIND_GUST_10METRE_NAME = 'wind_gust_10m_agl_m_s01'

KNOWN_FIELD_NAMES = [
    TEMPERATURE_2METRE_NAME, DEWPOINT_2METRE_NAME, U_WIND_10METRE_NAME,
    V_WIND_10METRE_NAME, WIND_GUST_10METRE_NAME
]


def is_wind_gust(field_name):
    """Returns Boolean flag to indicate whether variable is wind gust.

    :param field_name: Name of target variable.
    :return: is_wind_gust: Boolean flag.
    """

    # TODO(thunderhoser): This needs work.  10-m gust is not the only possible
    # gust variable.

    error_checking.assert_is_string(field_name)
    return field_name == WIND_GUST_10METRE_NAME


def is_wind_component(field_name):
    """Returns Boolean flag to indicate whether variable is u- or v-wind.

    :param field_name: Name of target variable.
    :return: is_wind_component: Boolean flag.
    """

    # TODO(thunderhoser): This needs work.  10-metre u and v are not the only
    # possible wind components.

    error_checking.assert_is_string(field_name)
    return field_name in [U_WIND_10METRE_NAME, V_WIND_10METRE_NAME]


def is_actually_stored_in_celsius(field_name):
    """Returns Boolean flag to indicate whether variable is stored in deg C.

    :param field_name: Name of target variable.
    :return: is_actually_stored_in_celsius: Boolean flag.
    """

    return field_name in [TEMPERATURE_2METRE_NAME, DEWPOINT_2METRE_NAME]
