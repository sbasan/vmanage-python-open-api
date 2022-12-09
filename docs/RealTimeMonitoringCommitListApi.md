# openapi_client.RealTimeMonitoringCommitListApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_configuration_commit_list**](RealTimeMonitoringCommitListApi.md#get_device_configuration_commit_list) | **GET** /device/configuration/commit-list | 


# **get_device_configuration_commit_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_configuration_commit_list(device_id)



Get device commit list

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_commit_list_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_commit_list_api.RealTimeMonitoringCommitListApi(api_client)
    device_id = "169.254.10.10" # str | deviceId - Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_configuration_commit_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCommitListApi->get_device_configuration_commit_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId - Device IP |

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

