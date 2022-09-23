# SensorCommunityApi.V1Api

All URIs are relative to *https://data.sensor.community*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataByApiID**](V1Api.md#getDataByApiID) | **GET** /airrohr/v1/sensor/{apiID} | All measurements of the last 5 minutes for one sensor
[**getDataLast5Minutes**](V1Api.md#getDataLast5Minutes) | **GET** /static/v1/data.json | Average of all measurements per sensor of the last 5 minutes for all.
[**getSensorValuesWithFilter**](V1Api.md#getSensorValuesWithFilter) | **GET** /airrohr/v1/filter/{query} | All measurements of the last 5 minutes filtered by query.



## getDataByApiID

> String getDataByApiID(apiID)

All measurements of the last 5 minutes for one sensor

All measurements of the last 5 minutes for one sensor. (NOT chipID. API-ID can be found by clicking on your sensor on the Map).

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V1Api();
let apiID = 37987; // Number | 
apiInstance.getDataByApiID(apiID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiID** | **Number**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataLast5Minutes

> String getDataLast5Minutes()

Average of all measurements per sensor of the last 5 minutes for all.

Average of all measurements per sensor of the last 5 minutes for all. Be careful (large response)! Do not use this in the OpenAPI UI!

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V1Api();
apiInstance.getDataLast5Minutes((error, data, response) => {
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


## getSensorValuesWithFilter

> String getSensorValuesWithFilter(query)

All measurements of the last 5 minutes filtered by query.

All measurements of the last 5 minutes filtered by query.

### Example

```javascript
import SensorCommunityApi from 'sensor_community_api';

let apiInstance = new SensorCommunityApi.V1Api();
let query = country=DE; // String | 
apiInstance.getSensorValuesWithFilter(query, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

