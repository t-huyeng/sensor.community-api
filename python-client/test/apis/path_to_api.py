import typing_extensions

from test.paths import PathValues
from test.apis.paths.static_v1_data_json import StaticV1DataJson
from test.apis.paths.airrohr_v1_filter_query import AirrohrV1FilterQuery
from test.apis.paths.airrohr_v1_sensor_api_id import AirrohrV1SensorApiID
from test.apis.paths.static_v2_data_json import StaticV2DataJson
from test.apis.paths.static_v2_data_1h_json import StaticV2Data1hJson
from test.apis.paths.static_v2_data_24h_json import StaticV2Data24hJson
from test.apis.paths.static_v2_data_dust_min_json import StaticV2DataDustMinJson
from test.apis.paths.static_v2_data_temp_min_json import StaticV2DataTempMinJson

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.STATIC_V1_DATA_JSON: StaticV1DataJson,
        PathValues.AIRROHR_V1_FILTER_QUERY: AirrohrV1FilterQuery,
        PathValues.AIRROHR_V1_SENSOR_API_ID: AirrohrV1SensorApiID,
        PathValues.STATIC_V2_DATA_JSON: StaticV2DataJson,
        PathValues.STATIC_V2_DATA_1H_JSON: StaticV2Data1hJson,
        PathValues.STATIC_V2_DATA_24H_JSON: StaticV2Data24hJson,
        PathValues.STATIC_V2_DATA_DUST_MIN_JSON: StaticV2DataDustMinJson,
        PathValues.STATIC_V2_DATA_TEMP_MIN_JSON: StaticV2DataTempMinJson,
    }
)

path_to_api = PathToApi(
    {
        PathValues.STATIC_V1_DATA_JSON: StaticV1DataJson,
        PathValues.AIRROHR_V1_FILTER_QUERY: AirrohrV1FilterQuery,
        PathValues.AIRROHR_V1_SENSOR_API_ID: AirrohrV1SensorApiID,
        PathValues.STATIC_V2_DATA_JSON: StaticV2DataJson,
        PathValues.STATIC_V2_DATA_1H_JSON: StaticV2Data1hJson,
        PathValues.STATIC_V2_DATA_24H_JSON: StaticV2Data24hJson,
        PathValues.STATIC_V2_DATA_DUST_MIN_JSON: StaticV2DataDustMinJson,
        PathValues.STATIC_V2_DATA_TEMP_MIN_JSON: StaticV2DataTempMinJson,
    }
)
