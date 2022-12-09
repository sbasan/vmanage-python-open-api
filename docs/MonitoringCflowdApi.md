# openapi_client.MonitoringCflowdApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cflow_collector_list**](MonitoringCflowdApi.md#create_cflow_collector_list) | **GET** /device/cflowd/flows | 
[**create_cflowd_collector_list**](MonitoringCflowdApi.md#create_cflowd_collector_list) | **GET** /device/cflowd/collector | 
[**create_cflowd_flows_count_list**](MonitoringCflowdApi.md#create_cflowd_flows_count_list) | **GET** /device/cflowd/flows-count | 
[**create_cflowd_statistics**](MonitoringCflowdApi.md#create_cflowd_statistics) | **GET** /device/cflowd/statistics | 
[**create_cflowd_template**](MonitoringCflowdApi.md#create_cflowd_template) | **GET** /device/cflowd/template | 
[**create_flow_device_data**](MonitoringCflowdApi.md#create_flow_device_data) | **GET** /statistics/cflowd/device/applications | 
[**create_flows_grid**](MonitoringCflowdApi.md#create_flows_grid) | **GET** /statistics/cflowd/applications | 
[**create_flowssummary**](MonitoringCflowdApi.md#create_flowssummary) | **GET** /statistics/cflowd/applications/summary | 
[**get_aggregation_data_by_query8**](MonitoringCflowdApi.md#get_aggregation_data_by_query8) | **GET** /statistics/cflowd/aggregation | 
[**get_cflowd_dpi_device_field_json**](MonitoringCflowdApi.md#get_cflowd_dpi_device_field_json) | **GET** /device/cflowd/application/fields | 
[**get_cflowd_dpi_field_json**](MonitoringCflowdApi.md#get_cflowd_dpi_field_json) | **GET** /device/cflowd/device/fields | 
[**get_count10**](MonitoringCflowdApi.md#get_count10) | **GET** /statistics/cflowd/doccount | 
[**get_count_post10**](MonitoringCflowdApi.md#get_count_post10) | **POST** /statistics/cflowd/doccount | 
[**get_fn_f_cache_stats**](MonitoringCflowdApi.md#get_fn_f_cache_stats) | **GET** /device/cflowd/fnf/cache-stats | 
[**get_fn_f_export_client_stats**](MonitoringCflowdApi.md#get_fn_f_export_client_stats) | **GET** /device/cflowd/fnf/export-client-stats | 
[**get_fn_f_export_stats**](MonitoringCflowdApi.md#get_fn_f_export_stats) | **GET** /device/cflowd/fnf/export-stats | 
[**get_fn_f_monitor_stats**](MonitoringCflowdApi.md#get_fn_f_monitor_stats) | **GET** /device/cflowd/fnf/monitor-stats | 
[**get_fnf**](MonitoringCflowdApi.md#get_fnf) | **GET** /device/cflowd/fnf/flow-monitor | 
[**get_post_aggregation_app_data_by_query8**](MonitoringCflowdApi.md#get_post_aggregation_app_data_by_query8) | **POST** /statistics/cflowd/app-agg/aggregation | 
[**get_post_aggregation_data_by_query8**](MonitoringCflowdApi.md#get_post_aggregation_data_by_query8) | **POST** /statistics/cflowd/aggregation | 
[**get_post_stat_bulk_raw_data8**](MonitoringCflowdApi.md#get_post_stat_bulk_raw_data8) | **POST** /statistics/cflowd/page | 
[**get_stat_bulk_raw_data8**](MonitoringCflowdApi.md#get_stat_bulk_raw_data8) | **GET** /statistics/cflowd/page | 
[**get_stat_data_fields10**](MonitoringCflowdApi.md#get_stat_data_fields10) | **GET** /statistics/cflowd/fields | 
[**get_stat_data_raw_data8**](MonitoringCflowdApi.md#get_stat_data_raw_data8) | **GET** /statistics/cflowd | 
[**get_stat_data_raw_data_as_csv8**](MonitoringCflowdApi.md#get_stat_data_raw_data_as_csv8) | **GET** /statistics/cflowd/csv | 
[**get_stat_query_fields10**](MonitoringCflowdApi.md#get_stat_query_fields10) | **GET** /statistics/cflowd/query/fields | 
[**get_stats_raw_data8**](MonitoringCflowdApi.md#get_stats_raw_data8) | **POST** /statistics/cflowd | 


# **create_cflow_collector_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_cflow_collector_list(device_id)



Get list of cflowd flows from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    src_ip = "src-ip_example" # str | Source IP (optional)
    dest_ip = "dest-ip_example" # str | Destination IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflow_collector_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflow_collector_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cflow_collector_list(device_id, vpn_id=vpn_id, src_ip=src_ip, dest_ip=dest_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflow_collector_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **src_ip** | **str**| Source IP | [optional]
 **dest_ip** | **str**| Destination IP | [optional]

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

# **create_cflowd_collector_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_cflowd_collector_list(device_id)



Get cflowd collector list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_collector_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflowd_collector_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

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

# **create_cflowd_flows_count_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_flows_count_list(device_id)



Get cflowd flow count from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    src_ip = "src-ip_example" # str | Source IP (optional)
    dest_ip = "dest-ip_example" # str | Destination IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_flows_count_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflowd_flows_count_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cflowd_flows_count_list(device_id, vpn_id=vpn_id, src_ip=src_ip, dest_ip=dest_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflowd_flows_count_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **src_ip** | **str**| Source IP | [optional]
 **dest_ip** | **str**| Destination IP | [optional]

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

# **create_cflowd_statistics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_statistics(device_id)



Get cflowd statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_statistics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflowd_statistics: %s\n" % e)
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

# **create_cflowd_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_template(device_id)



Get cflowd template from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_template(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_cflowd_template: %s\n" % e)
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

# **create_flow_device_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_flow_device_data()



Generate cflowd flows list in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_flow_device_data(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_flow_device_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query | [optional]

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

# **create_flows_grid**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_flows_grid()



Generate cflowd flows list in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    vpn = "vpn_example" # str | VPN Id (optional)
    device_id = "00r252U250?250" # str | Device IP (optional)
    limit = 1 # int | Limit (optional)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_flows_grid(vpn=vpn, device_id=device_id, limit=limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_flows_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn** | **str**| VPN Id | [optional]
 **device_id** | **str**| Device IP | [optional]
 **limit** | **int**| Limit | [optional]
 **query** | **str**| Query | [optional]

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

# **create_flowssummary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_flowssummary()



Generate cflowd flows list in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    limit = 1 # int | Limit (optional)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_flowssummary(limit=limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->create_flowssummary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit | [optional]
 **query** | **str**| Query | [optional]

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

# **get_aggregation_data_by_query8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query8()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query8(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_aggregation_data_by_query8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]

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

# **get_cflowd_dpi_device_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cflowd_dpi_device_field_json()



Get Cflowd DPI query field JSON

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    is_device_dash_board = False # bool | Flag whether it is device dashboard request (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cflowd_dpi_device_field_json(is_device_dash_board=is_device_dash_board)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_cflowd_dpi_device_field_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_device_dash_board** | **bool**| Flag whether it is device dashboard request | [optional] if omitted the server will use the default value of False

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

# **get_cflowd_dpi_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cflowd_dpi_field_json()



Get CflowdvDPI query field JSON

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    is_device_dash_board = False # bool | Flag whether it is device dashboard request (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cflowd_dpi_field_json(is_device_dash_board=is_device_dash_board)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_cflowd_dpi_field_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_device_dash_board** | **bool**| Flag whether it is device dashboard request | [optional] if omitted the server will use the default value of False

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

# **get_count10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count10(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2021-05-10T01:00:00 UTC","2021-11-30T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count10(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_count10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

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

# **get_count_post10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post10()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post10(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_count_post10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query | [optional]

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

# **get_fn_f_cache_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_cache_stats(device_id)



Get FnF cache stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_cache_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_fn_f_cache_stats: %s\n" % e)
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

# **get_fn_f_export_client_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_export_client_stats(device_id)



Get FnF export client stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_export_client_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_fn_f_export_client_stats: %s\n" % e)
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

# **get_fn_f_export_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_export_stats(device_id)



Get FnF export stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_export_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_fn_f_export_stats: %s\n" % e)
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

# **get_fn_f_monitor_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_monitor_stats(device_id)



Get FnF monitor stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_monitor_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_fn_f_monitor_stats: %s\n" % e)
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

# **get_fnf**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fnf(device_id)



Get FnF from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fnf(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_fnf: %s\n" % e)
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

# **get_post_aggregation_app_data_by_query8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query8()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query8(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_post_aggregation_app_data_by_query8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_aggregation_data_by_query8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query8()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query8(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_post_aggregation_data_by_query8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_stat_bulk_raw_data8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data8()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data8(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_post_stat_bulk_raw_data8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_stat_bulk_raw_data8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data8()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data8(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stat_bulk_raw_data8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]

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

# **get_stat_data_fields10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields10()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields10()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stat_data_fields10: %s\n" % e)
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

# **get_stat_data_raw_data8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data8()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by(emp:entry_time) (optional)
    sort_order = "sortOrder_example" # str | sort order(emp:asc、ASC、Asc、desc、Desc、DESC) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data8(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stat_data_raw_data8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by(emp:entry_time) | [optional]
 **sort_order** | **str**| sort order(emp:asc、ASC、Asc、desc、Desc、DESC) | [optional]

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

# **get_stat_data_raw_data_as_csv8**
> str get_stat_data_raw_data_as_csv8()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv8(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stat_data_raw_data_as_csv8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_query_fields10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields10()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields10()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stat_query_fields10: %s\n" % e)
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

# **get_stats_raw_data8**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data8()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_api.MonitoringCflowdApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data8(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdApi->get_stats_raw_data8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

