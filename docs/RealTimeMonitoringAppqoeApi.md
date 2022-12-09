# openapi_client.RealTimeMonitoringAppqoeApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appqoe_active_flow_id_details**](RealTimeMonitoringAppqoeApi.md#create_appqoe_active_flow_id_details) | **GET** /device/appqoe/active-flow-id | 
[**create_appqoe_flow_id_expired_details**](RealTimeMonitoringAppqoeApi.md#create_appqoe_flow_id_expired_details) | **GET** /device/appqoe/expired-flow-id | 
[**create_appqoe_vpn_id_list**](RealTimeMonitoringAppqoeApi.md#create_appqoe_vpn_id_list) | **GET** /device/appqoe/vpn-id | 
[**get_appqoe_cluster_summary**](RealTimeMonitoringAppqoeApi.md#get_appqoe_cluster_summary) | **GET** /device/appqoe/cluster-summary | 
[**get_appqoe_error_recent**](RealTimeMonitoringAppqoeApi.md#get_appqoe_error_recent) | **GET** /device/appqoe/error-recent | 
[**get_appqoe_expired**](RealTimeMonitoringAppqoeApi.md#get_appqoe_expired) | **GET** /device/appqoe/flow-expired | 
[**get_appqoe_flow_closed_error**](RealTimeMonitoringAppqoeApi.md#get_appqoe_flow_closed_error) | **GET** /device/appqoe/flow-closed-error | 
[**get_appqoe_hput_stats**](RealTimeMonitoringAppqoeApi.md#get_appqoe_hput_stats) | **GET** /device/appqoe/appqoe-hput-stats | 
[**get_appqoe_nat_stats**](RealTimeMonitoringAppqoeApi.md#get_appqoe_nat_stats) | **GET** /device/appqoe/appqoe-nat-stats | 
[**get_appqoe_rm_resources**](RealTimeMonitoringAppqoeApi.md#get_appqoe_rm_resources) | **GET** /device/appqoe/appqoe-rm-resource | 
[**get_appqoe_rm_stats**](RealTimeMonitoringAppqoeApi.md#get_appqoe_rm_stats) | **GET** /device/appqoe/appqoe-rm-stats | 
[**get_appqoe_service_controllers**](RealTimeMonitoringAppqoeApi.md#get_appqoe_service_controllers) | **GET** /device/appqoe/service-controllers | 
[**get_appqoe_services_status**](RealTimeMonitoringAppqoeApi.md#get_appqoe_services_status) | **GET** /device/appqoe/appqoe-services-status | 
[**get_appqoe_sppi_pipe_stats**](RealTimeMonitoringAppqoeApi.md#get_appqoe_sppi_pipe_stats) | **GET** /device/appqoe/appqoe-sppi-pipe-resource | 
[**get_appqoe_sppi_queue_stats**](RealTimeMonitoringAppqoeApi.md#get_appqoe_sppi_queue_stats) | **GET** /device/appqoe/appqoe-sppi-queue-resource | 
[**get_appqoe_status**](RealTimeMonitoringAppqoeApi.md#get_appqoe_status) | **GET** /device/appqoe/status | 


# **create_appqoe_active_flow_id_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_appqoe_active_flow_id_details(flow_id, device_id)



Get Appqoe Active flow Id details from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    flow_id = "flow-id_example" # str | Flow Id
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_appqoe_active_flow_id_details(flow_id, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->create_appqoe_active_flow_id_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**| Flow Id |
 **device_id** | **str**| Device IP |

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

# **create_appqoe_flow_id_expired_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_appqoe_flow_id_expired_details(flow_id, device_id)



Get Appqoe Expired flow Id details from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    flow_id = "flow-id_example" # str | Flow Id
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_appqoe_flow_id_expired_details(flow_id, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->create_appqoe_flow_id_expired_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**| Flow Id |
 **device_id** | **str**| Device IP |

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

# **create_appqoe_vpn_id_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_appqoe_vpn_id_list(vpn_id, device_id)



Get Appqoe Active vpn Id details from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    vpn_id = "vpn-id_example" # str | VPN Id
    device_id = "00r252U250?250" # str | Device IP
    client_ip = "client-ip_example" # str | Client Ip (optional)
    server_ip = "server-ip_example" # str | Server Ip (optional)
    server_port = "server-port_example" # str | Server-Port (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_appqoe_vpn_id_list(vpn_id, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->create_appqoe_vpn_id_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_appqoe_vpn_id_list(vpn_id, device_id, client_ip=client_ip, server_ip=server_ip, server_port=server_port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->create_appqoe_vpn_id_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **str**| VPN Id |
 **device_id** | **str**| Device IP |
 **client_ip** | **str**| Client Ip | [optional]
 **server_ip** | **str**| Server Ip | [optional]
 **server_port** | **str**| Server-Port | [optional]

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

# **get_appqoe_cluster_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_cluster_summary(device_id)



Get Appqoe Cluster Summary from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_cluster_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_cluster_summary: %s\n" % e)
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

# **get_appqoe_error_recent**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_error_recent(device_id)



Get Appqoe error recent from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_error_recent(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_error_recent: %s\n" % e)
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

# **get_appqoe_expired**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_expired(device_id)



Get Appqoe expired from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_expired(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_expired: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

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

# **get_appqoe_flow_closed_error**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_flow_closed_error(device_id)



Get Appqoe flow closed error from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_flow_closed_error(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_flow_closed_error: %s\n" % e)
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

# **get_appqoe_hput_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_hput_stats(device_id)



Get Appqoe Hput Statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_hput_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_hput_stats: %s\n" % e)
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

# **get_appqoe_nat_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_nat_stats(device_id)



Get Appqoe Nat Statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_nat_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_nat_stats: %s\n" % e)
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

# **get_appqoe_rm_resources**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_rm_resources(device_id)



Get Appqoe Resource Manager resources from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_rm_resources(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_rm_resources: %s\n" % e)
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

# **get_appqoe_rm_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_rm_stats(device_id)



Get Appqoe RM Statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_rm_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_rm_stats: %s\n" % e)
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

# **get_appqoe_service_controllers**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_service_controllers(device_id)



Get Appqoe service controllers from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_service_controllers(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_service_controllers: %s\n" % e)
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

# **get_appqoe_services_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_services_status(device_id)



Get Appqoe Services Status from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_services_status(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_services_status: %s\n" % e)
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

# **get_appqoe_sppi_pipe_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_sppi_pipe_stats(device_id)



Get Appqoe Sppi Pipe Stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_sppi_pipe_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_sppi_pipe_stats: %s\n" % e)
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

# **get_appqoe_sppi_queue_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_sppi_queue_stats(device_id)



Get Appqoe Sppi Queue Stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_sppi_queue_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_sppi_queue_stats: %s\n" % e)
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

# **get_appqoe_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_appqoe_status(device_id)



Get Appqoe status from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_appqoe_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_appqoe_api.RealTimeMonitoringAppqoeApi(api_client)
    device_id = "169.254.10.10" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_appqoe_status(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppqoeApi->get_appqoe_status: %s\n" % e)
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

