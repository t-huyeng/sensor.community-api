# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from test.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    STATIC_V1_DATA_JSON = "/static/v1/data.json"
    AIRROHR_V1_FILTER_QUERY = "/airrohr/v1/filter/{query}"
    AIRROHR_V1_SENSOR_API_ID = "/airrohr/v1/sensor/{apiID}"
    STATIC_V2_DATA_JSON = "/static/v2/data.json"
    STATIC_V2_DATA_1H_JSON = "/static/v2/data.1h.json"
    STATIC_V2_DATA_24H_JSON = "/static/v2/data.24h.json"
    STATIC_V2_DATA_DUST_MIN_JSON = "/static/v2/data.dust.min.json"
    STATIC_V2_DATA_TEMP_MIN_JSON = "/static/v2/data.temp.min.json"
