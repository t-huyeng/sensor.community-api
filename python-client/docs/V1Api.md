# sensorcommunity.V1Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_by_api_id**](V1Api.md#get_data_by_api_id) | **GET** /airrohr/v1/sensor/{apiID}/ | all measurements of the last 5 minutes for one sensor
[**get_data_last5_minutes**](V1Api.md#get_data_last5_minutes) | **GET** /static/v1/data.json | average of all measurements per sensor of the last 5 minutes for all.
[**get_sensor_values_with_filter**](V1Api.md#get_sensor_values_with_filter) | **GET** /airrohr/v1/filter/{query} | all measurements of the last 5 minutes filtered by query.


# **get_data_by_api_id**
> str get_data_by_api_id(api_id)

all measurements of the last 5 minutes for one sensor

all measurements of the last 5 minutes for one sensor. (NOT chipID. API-ID can be found by clicking on your sensor on the Map).

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)
    api_id = 37987 # int | 

    # example passing only required values which don't have defaults set
    try:
        # all measurements of the last 5 minutes for one sensor
        api_response = api_instance.get_data_by_api_id(api_id)
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V1Api->get_data_by_api_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **int**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_last5_minutes**
> str get_data_last5_minutes()

average of all measurements per sensor of the last 5 minutes for all.

average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the last 5 minutes for all.
        api_response = api_instance.get_data_last5_minutes()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V1Api->get_data_last5_minutes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensor_values_with_filter**
> str get_sensor_values_with_filter(query)

all measurements of the last 5 minutes filtered by query.

all measurements of the last 5 minutes filtered by query.

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v1_api.V1Api(api_client)
    query = "country=DE" # str | 

    # example passing only required values which don't have defaults set
    try:
        # all measurements of the last 5 minutes filtered by query.
        api_response = api_instance.get_sensor_values_with_filter(query)
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V1Api->get_sensor_values_with_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

