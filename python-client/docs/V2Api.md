# sensorcommunity.V2Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_last1_hour**](V2Api.md#get_data_last1_hour) | **GET** /static/v2/data.1h.json | average of all measurements per sensor of the last hour.
[**get_data_last24_hour**](V2Api.md#get_data_last24_hour) | **GET** /static/v2/data.24h.json | average of all measurements per sensor of the 24 hours.
[**get_data_last5_minutes_v2**](V2Api.md#get_data_last5_minutes_v2) | **GET** /static/v2/data.json | average of all measurements per sensor of the last 5 minutes for all.
[**get_dust_data_last5_minutes**](V2Api.md#get_dust_data_last5_minutes) | **GET** /static/v2/data.dust.min.json | average of all measurements per sensor of the last 5 minutes for all dust sensors only.
[**get_temp_hum_air_data_last5_minutes**](V2Api.md#get_temp_hum_air_data_last5_minutes) | **GET** /static/v2/data.temp.min.json | average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.


# **get_data_last1_hour**
> str get_data_last1_hour()

average of all measurements per sensor of the last hour.

average of all measurements per sensor of the last hour. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the last hour.
        api_response = api_instance.get_data_last1_hour()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V2Api->get_data_last1_hour: %s\n" % e)
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

# **get_data_last24_hour**
> str get_data_last24_hour()

average of all measurements per sensor of the 24 hours.

average of all measurements per sensor of the 24 hours. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the 24 hours.
        api_response = api_instance.get_data_last24_hour()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V2Api->get_data_last24_hour: %s\n" % e)
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

# **get_data_last5_minutes_v2**
> str get_data_last5_minutes_v2()

average of all measurements per sensor of the last 5 minutes for all.

average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the last 5 minutes for all.
        api_response = api_instance.get_data_last5_minutes_v2()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V2Api->get_data_last5_minutes_v2: %s\n" % e)
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

# **get_dust_data_last5_minutes**
> str get_dust_data_last5_minutes()

average of all measurements per sensor of the last 5 minutes for all dust sensors only.

average of all measurements per sensor of the last 5 minutes for all dust sensors only. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the last 5 minutes for all dust sensors only.
        api_response = api_instance.get_dust_data_last5_minutes()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V2Api->get_dust_data_last5_minutes: %s\n" % e)
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

# **get_temp_hum_air_data_last5_minutes**
> str get_temp_hum_air_data_last5_minutes()

average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.

average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only. Be careful (large response)!

### Example


```python
import time
from deutschland import sensorcommunity
from deutschland.sensorcommunity.api import v2_api
from pprint import pprint
# Defining the host is optional and defaults to https://data.sensor.community
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorcommunity.Configuration(
    host = "https://data.sensor.community"
)


# Enter a context with an instance of the API client
with sensorcommunity.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = v2_api.V2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.
        api_response = api_instance.get_temp_hum_air_data_last5_minutes()
        pprint(api_response)
    except sensorcommunity.ApiException as e:
        print("Exception when calling V2Api->get_temp_hum_air_data_last5_minutes: %s\n" % e)
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

