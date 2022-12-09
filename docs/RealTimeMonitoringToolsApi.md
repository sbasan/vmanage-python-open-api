# openapi_client.RealTimeMonitoringToolsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_tools_n_slookup**](RealTimeMonitoringToolsApi.md#get_device_tools_n_slookup) | **GET** /device/tools/nslookup | 
[**get_device_tools_netstat**](RealTimeMonitoringToolsApi.md#get_device_tools_netstat) | **GET** /device/tools/netstat | 
[**get_device_tools_ss**](RealTimeMonitoringToolsApi.md#get_device_tools_ss) | **GET** /device/tools/ss | 
[**get_real_timeinfo**](RealTimeMonitoringToolsApi.md#get_real_timeinfo) | **GET** /device/tools/realtimeinfo | 
[**get_system_netfilter**](RealTimeMonitoringToolsApi.md#get_system_netfilter) | **GET** /device/tools/system-netfilter | 


# **get_device_tools_n_slookup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tools_n_slookup(vpn, dns, device_id)



Get device tool nslookup

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tools_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tools_api.RealTimeMonitoringToolsApi(api_client)
    vpn = "0" # str | VPN
    dns = "8.8.8.8" # str | DNS
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_tools_n_slookup(vpn, dns, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_device_tools_n_slookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn** | **str**| VPN |
 **dns** | **str**| DNS |
 **device_id** | **str**| Device Id |

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

# **get_device_tools_netstat**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tools_netstat(device_id)



Get device tool net stat

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tools_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tools_api.RealTimeMonitoringToolsApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn = "0" # str | VPN (optional)
    options = "options_example" # str | Options (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_tools_netstat(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_device_tools_netstat: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_tools_netstat(device_id, vpn=vpn, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_device_tools_netstat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn** | **str**| VPN | [optional]
 **options** | **str**| Options | [optional]

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

# **get_device_tools_ss**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tools_ss(device_id)



Get device tool ss

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tools_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tools_api.RealTimeMonitoringToolsApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn = "0" # str | VPN (optional)
    options = "options_example" # str | Options (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_tools_ss(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_device_tools_ss: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_tools_ss(device_id, vpn=vpn, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_device_tools_ss: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn** | **str**| VPN | [optional]
 **options** | **str**| Options | [optional]

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

# **get_real_timeinfo**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_real_timeinfo(device_id)



Get hardware real time info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tools_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tools_api.RealTimeMonitoringToolsApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_real_timeinfo(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_real_timeinfo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

# **get_system_netfilter**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_system_netfilter(device_id)



Get system netfilter info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tools_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tools_api.RealTimeMonitoringToolsApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_system_netfilter(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringToolsApi->get_system_netfilter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

