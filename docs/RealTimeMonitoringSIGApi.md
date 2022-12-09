# openapi_client.RealTimeMonitoringSIGApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sig_tunnel_list**](RealTimeMonitoringSIGApi.md#get_sig_tunnel_list) | **GET** /device/sig/getSigTunnelList | 
[**get_sig_tunnel_total**](RealTimeMonitoringSIGApi.md#get_sig_tunnel_total) | **GET** /device/sig/getSigTunnelTotal | 
[**get_sig_umbrella_tunnels**](RealTimeMonitoringSIGApi.md#get_sig_umbrella_tunnels) | **GET** /device/sig/umbrella/tunnels | 
[**get_sig_zscaler_tunnels**](RealTimeMonitoringSIGApi.md#get_sig_zscaler_tunnels) | **GET** /device/sig/zscaler/tunnels | 
[**tunnel_dashboard**](RealTimeMonitoringSIGApi.md#tunnel_dashboard) | **GET** /device/sig/tunnelDashboard | 


# **get_sig_tunnel_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sig_tunnel_list()



get Sig TunnelList

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sig_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sig_api.RealTimeMonitoringSIGApi(api_client)
    page_size = "pageSize_example" # str | Page Size (optional)
    offset = "offset_example" # str | Page offset (optional)
    last_n_hours = "lastNHours_example" # str | last n hours (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sig_tunnel_list(page_size=page_size, offset=offset, last_n_hours=last_n_hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSIGApi->get_sig_tunnel_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **str**| Page Size | [optional]
 **offset** | **str**| Page offset | [optional]
 **last_n_hours** | **str**| last n hours | [optional]

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

# **get_sig_tunnel_total**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sig_tunnel_total()



get Sig Tunnel Total coount

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sig_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sig_api.RealTimeMonitoringSIGApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_sig_tunnel_total()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSIGApi->get_sig_tunnel_total: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_sig_umbrella_tunnels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sig_umbrella_tunnels(device_id)



Get SIG Umbrella tunnels from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sig_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sig_api.RealTimeMonitoringSIGApi(api_client)
    device_id = "169.254.10.10" # str | deviceId - Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sig_umbrella_tunnels(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSIGApi->get_sig_umbrella_tunnels: %s\n" % e)
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

# **get_sig_zscaler_tunnels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sig_zscaler_tunnels(device_id)



Get SIG Zscaler tunnels from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sig_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sig_api.RealTimeMonitoringSIGApi(api_client)
    device_id = "169.254.10.10" # str | deviceId - Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sig_zscaler_tunnels(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSIGApi->get_sig_zscaler_tunnels: %s\n" % e)
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

# **tunnel_dashboard**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} tunnel_dashboard()



Get SIG Zscaler tunnels from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sig_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sig_api.RealTimeMonitoringSIGApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tunnel_dashboard()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSIGApi->tunnel_dashboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

