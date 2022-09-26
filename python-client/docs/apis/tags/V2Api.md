<a name="__pageTop"></a>
# test.apis.tags.v2_api.V2Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_last1_hour**](#get_data_last1_hour) | **get** /static/v2/data.1h.json | Average of all measurements per sensor of the last hour.
[**get_data_last24_hour**](#get_data_last24_hour) | **get** /static/v2/data.24h.json | Average of all measurements per sensor of the 24 hours.
[**get_data_last5_minutes_v2**](#get_data_last5_minutes_v2) | **get** /static/v2/data.json | Average of all measurements per sensor of the last 5 minutes for all.
[**get_dust_data_last5_minutes**](#get_dust_data_last5_minutes) | **get** /static/v2/data.dust.min.json | Average of all measurements per sensor of the last 5 minutes for all dust sensors only.
[**get_temp_hum_air_data_last5_minutes**](#get_temp_hum_air_data_last5_minutes) | **get** /static/v2/data.temp.min.json | Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.

# **get_data_last1_hour**
<a name="get_data_last1_hour"></a>
> str get_data_last1_hour()

Average of all measurements per sensor of the last hour.

Average of all measurements per sensor of the last hour. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the last hour.
        api_response = api_instance.get_data_last1_hour()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V2Api->get_data_last1_hour: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_last1_hour.ApiResponseFor200) | OK

#### get_data_last1_hour.ApiResponseFor200
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

# **get_data_last24_hour**
<a name="get_data_last24_hour"></a>
> str get_data_last24_hour()

Average of all measurements per sensor of the 24 hours.

Average of all measurements per sensor of the 24 hours. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the 24 hours.
        api_response = api_instance.get_data_last24_hour()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V2Api->get_data_last24_hour: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_last24_hour.ApiResponseFor200) | OK

#### get_data_last24_hour.ApiResponseFor200
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

# **get_data_last5_minutes_v2**
<a name="get_data_last5_minutes_v2"></a>
> str get_data_last5_minutes_v2()

Average of all measurements per sensor of the last 5 minutes for all.

Average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the last 5 minutes for all.
        api_response = api_instance.get_data_last5_minutes_v2()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V2Api->get_data_last5_minutes_v2: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_last5_minutes_v2.ApiResponseFor200) | OK

#### get_data_last5_minutes_v2.ApiResponseFor200
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

# **get_dust_data_last5_minutes**
<a name="get_dust_data_last5_minutes"></a>
> str get_dust_data_last5_minutes()

Average of all measurements per sensor of the last 5 minutes for all dust sensors only.

Average of all measurements per sensor of the last 5 minutes for all dust sensors only. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the last 5 minutes for all dust sensors only.
        api_response = api_instance.get_dust_data_last5_minutes()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V2Api->get_dust_data_last5_minutes: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dust_data_last5_minutes.ApiResponseFor200) | OK

#### get_dust_data_last5_minutes.ApiResponseFor200
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

# **get_temp_hum_air_data_last5_minutes**
<a name="get_temp_hum_air_data_last5_minutes"></a>
> str get_temp_hum_air_data_last5_minutes()

Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.

Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```python
import test
from test.apis.tags import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = test.Configuration(
    host = "https://data.sensor.community"
)

# Enter a context with an instance of the API client
with test.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.
        api_response = api_instance.get_temp_hum_air_data_last5_minutes()
        pprint(api_response)
    except test.ApiException as e:
        print("Exception when calling V2Api->get_temp_hum_air_data_last5_minutes: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_temp_hum_air_data_last5_minutes.ApiResponseFor200) | OK

#### get_temp_hum_air_data_last5_minutes.ApiResponseFor200
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

