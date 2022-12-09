# openapi_client.ConfigurationDeviceConnectivityApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invalidate_device**](ConfigurationDeviceConnectivityApi.md#invalidate_device) | **POST** /certificate/device/invalidate | 
[**stage_device**](ConfigurationDeviceConnectivityApi.md#stage_device) | **POST** /certificate/device/stage | 


# **invalidate_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} invalidate_device()



invalidate the device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_connectivity_api.ConfigurationDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.invalidate_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceConnectivityApi->invalidate_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device info | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stage_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stage_device()



Stop data traffic to device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_connectivity_api.ConfigurationDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.stage_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceConnectivityApi->stage_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device info | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

