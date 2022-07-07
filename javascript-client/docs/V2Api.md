# SensorCommunityApi.V2Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataLast1Hour**](V2Api.md#getDataLast1Hour) | **GET** /static/v2/data.1h.json | Average of all measurements per sensor of the last hour.
[**getDataLast24Hour**](V2Api.md#getDataLast24Hour) | **GET** /static/v2/data.24h.json | Average of all measurements per sensor of the 24 hours.
[**getDataLast5MinutesV2**](V2Api.md#getDataLast5MinutesV2) | **GET** /static/v2/data.json | Average of all measurements per sensor of the last 5 minutes for all.
[**getDustDataLast5Minutes**](V2Api.md#getDustDataLast5Minutes) | **GET** /static/v2/data.dust.min.json | Average of all measurements per sensor of the last 5 minutes for all dust sensors only.
[**getTempHumAirDataLast5Minutes**](V2Api.md#getTempHumAirDataLast5Minutes) | **GET** /static/v2/data.temp.min.json | Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.



## getDataLast1Hour

> String getDataLast1Hour()

Average of all measurements per sensor of the last hour.

Average of all measurements per sensor of the last hour. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V2Api();
apiInstance.getDataLast1Hour((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataLast24Hour

> String getDataLast24Hour()

Average of all measurements per sensor of the 24 hours.

Average of all measurements per sensor of the 24 hours. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V2Api();
apiInstance.getDataLast24Hour((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataLast5MinutesV2

> String getDataLast5MinutesV2()

Average of all measurements per sensor of the last 5 minutes for all.

Average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V2Api();
apiInstance.getDataLast5MinutesV2((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDustDataLast5Minutes

> String getDustDataLast5Minutes()

Average of all measurements per sensor of the last 5 minutes for all dust sensors only.

Average of all measurements per sensor of the last 5 minutes for all dust sensors only. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V2Api();
apiInstance.getDustDataLast5Minutes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTempHumAirDataLast5Minutes

> String getTempHumAirDataLast5Minutes()

Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.

Average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V2Api();
apiInstance.getTempHumAirDataLast5Minutes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

