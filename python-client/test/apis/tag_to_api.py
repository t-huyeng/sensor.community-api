import typing_extensions

from test.apis.tags import TagValues
from test.apis.tags.v1_api import V1Api
from test.apis.tags.v2_api import V2Api

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.V1: V1Api,
        TagValues.V2: V2Api,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.V1: V1Api,
        TagValues.V2: V2Api,
    }
)
