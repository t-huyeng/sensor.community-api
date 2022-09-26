<a name="__pageTop"></a>
# test.apis.tags.v1_api.V1Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_by_api_id**](#get_data_by_api_id) | **get** /airrohr/v1/sensor/{apiID} | All measurements of the last 5 minutes for one sensor
[**get_data_last5_minutes**](#get_data_last5_minutes) | **get** /static/v1/data.json | Average of all measurements per sensor of the last 5 minutes for all.
[**get_sensor_values_with_filter**](#get_sensor_values_with_filter) | **get** /airrohr/v1/filter/{query} | All measurements of the last 5 minutes filtered by query.

# **get_data_by_api_id**
<a name="get_data_by_api_id"></a>
> str get_data_by_api_id(api_id)

All measurements of the last 5 minutes for one sensor

All measurements of the last 5 minutes for one sensor. (NOT chipID. API-ID can be found by clicking on your sensor on the Map).

### Example

```python
import test
from test.apis.tags import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'apiID': 37987,
    }
    try:
        # All measurements of the last 5 minutes for one sensor
        api_response = api_instance.get_data_by_api_id(
            path_params=path_params,
        )
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V1Api->get_data_by_api_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
apiID | ApiIDSchema | | 

# ApiIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_by_api_id.ApiResponseFor200) | OK

#### get_data_by_api_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_data_last5_minutes**
<a name="get_data_last5_minutes"></a>
> str get_data_last5_minutes()

Average of all measurements per sensor of the last 5 minutes for all.

Average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the last 5 minutes for all.
        api_response = api_instance.get_data_last5_minutes()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V1Api->get_data_last5_minutes: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_last5_minutes.ApiResponseFor200) | OK

#### get_data_last5_minutes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sensor_values_with_filter**
<a name="get_sensor_values_with_filter"></a>
> str get_sensor_values_with_filter(query)

All measurements of the last 5 minutes filtered by query.

All measurements of the last 5 minutes filtered by query.

### Example

```python
import test
from test.apis.tags import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'query': "country=DE",
    }
    try:
        # All measurements of the last 5 minutes filtered by query.
        api_response = api_instance.get_sensor_values_with_filter(
            path_params=path_params,
        )
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V1Api->get_sensor_values_with_filter: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sensor_values_with_filter.ApiResponseFor200) | OK

#### get_sensor_values_with_filter.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

