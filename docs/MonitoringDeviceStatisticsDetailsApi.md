# openapi_client.MonitoringDeviceStatisticsDetailsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_device_statistics_data**](MonitoringDeviceStatisticsDetailsApi.md#generate_device_statistics_data) | **GET** /data/device/statistics/{state_data_type} | 
[**get_active_alarms**](MonitoringDeviceStatisticsDetailsApi.md#get_active_alarms) | **GET** /data/device/statistics/alarm/active | 
[**get_count_with_state_data_type**](MonitoringDeviceStatisticsDetailsApi.md#get_count_with_state_data_type) | **GET** /data/device/statistics/{state_data_type}/doccount | 
[**get_stat_data_fields_by_state_data_type**](MonitoringDeviceStatisticsDetailsApi.md#get_stat_data_fields_by_state_data_type) | **GET** /data/device/statistics/{state_data_type}/fields | 
[**get_statistics_type**](MonitoringDeviceStatisticsDetailsApi.md#get_statistics_type) | **GET** /data/device/statistics | 


# **generate_device_statistics_data**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_device_statistics_data(state_data_type)



Get device statistics data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_statistics_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_statistics_details_api.MonitoringDeviceStatisticsDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type
    scroll_id = "scrollId_example" # str | Scroll Id (optional)
    start_date = "startDate_example" # str | Start date (optional)
    end_date = "endDate_example" # str | End date (optional)
    count = 1 # int |  (optional)
    time_zone = "timeZone_example" # str | Time zone (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_statistics_data(state_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->generate_device_statistics_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_device_statistics_data(state_data_type, scroll_id=scroll_id, start_date=start_date, end_date=end_date, count=count, time_zone=time_zone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->generate_device_statistics_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type |
 **scroll_id** | **str**| Scroll Id | [optional]
 **start_date** | **str**| Start date | [optional]
 **end_date** | **str**| End date | [optional]
 **count** | **int**|  | [optional]
 **time_zone** | **str**| Time zone | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_alarms**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_active_alarms(scroll_id)



Get active alarms

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_statistics_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_statistics_details_api.MonitoringDeviceStatisticsDetailsApi(api_client)
    scroll_id = "scrollId_example" # str | SrollId
    start_date = "startDate_example" # str | Start date (optional)
    end_date = "endDate_example" # str | End date (optional)
    count = 1 # int | count (optional)
    time_zone = "timeZone_example" # str | Time zone (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_active_alarms(scroll_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_active_alarms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_active_alarms(scroll_id, start_date=start_date, end_date=end_date, count=count, time_zone=time_zone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_active_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| SrollId |
 **start_date** | **str**| Start date | [optional]
 **end_date** | **str**| End date | [optional]
 **count** | **int**| count | [optional]
 **time_zone** | **str**| Time zone | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_with_state_data_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_with_state_data_type(state_data_type, start_date, end_date)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_statistics_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_statistics_details_api.MonitoringDeviceStatisticsDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type(example:object)
    start_date = "startDate_example" # str | Start date (example:2021-1-1T00:00:00)
    end_date = "endDate_example" # str | End date (example:2021-12-1T00:00:00)
    time_zone = "timeZone_example" # str | Time zone (example:UTC) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count_with_state_data_type(state_data_type, start_date, end_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_count_with_state_data_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_with_state_data_type(state_data_type, start_date, end_date, time_zone=time_zone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_count_with_state_data_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type(example:object) |
 **start_date** | **str**| Start date (example:2021-1-1T00:00:00) |
 **end_date** | **str**| End date (example:2021-12-1T00:00:00) |
 **time_zone** | **str**| Time zone (example:UTC) | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_data_fields_by_state_data_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_stat_data_fields_by_state_data_type(state_data_type)



Get statistics fields and types

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_statistics_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_statistics_details_api.MonitoringDeviceStatisticsDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stat_data_fields_by_state_data_type(state_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_stat_data_fields_by_state_data_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_statistics_type()



Get statistics types

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_statistics_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_statistics_details_api.MonitoringDeviceStatisticsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_statistics_type()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceStatisticsDetailsApi->get_statistics_type: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

