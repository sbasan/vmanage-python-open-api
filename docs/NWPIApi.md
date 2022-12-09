# openapi_client.NWPIApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agg_flow**](NWPIApi.md#get_agg_flow) | **GET** /stream/device/nwpi/aggFlow | 
[**get_app_qos_data**](NWPIApi.md#get_app_qos_data) | **GET** /stream/device/nwpi/appQosData | 
[**get_app_qos_state**](NWPIApi.md#get_app_qos_state) | **GET** /stream/device/nwpi/appQosState | 
[**get_concurrent_data**](NWPIApi.md#get_concurrent_data) | **GET** /stream/device/nwpi/concurrentData | 
[**get_concurrent_domain_data**](NWPIApi.md#get_concurrent_domain_data) | **GET** /stream/device/nwpi/concurrentDomainData | 
[**get_event_app_hop_list**](NWPIApi.md#get_event_app_hop_list) | **GET** /stream/device/nwpi/eventAppHopList | 
[**get_event_app_score_bandwidth**](NWPIApi.md#get_event_app_score_bandwidth) | **GET** /stream/device/nwpi/eventAppScoreBandwidth | 
[**get_event_flow_from_app_hop**](NWPIApi.md#get_event_flow_from_app_hop) | **GET** /stream/device/nwpi/eventFlowFromAppHop | 
[**get_event_readout**](NWPIApi.md#get_event_readout) | **GET** /stream/device/nwpi/eventReadout | 
[**get_routing_detail_from_local**](NWPIApi.md#get_routing_detail_from_local) | **GET** /stream/device/nwpi/routingDetail | 


# **get_agg_flow**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_agg_flow(trace_id, timestamp, trace_state)



Get aggregated flow data for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    trace_state = "traceState_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_agg_flow(trace_id, timestamp, trace_state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_agg_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **trace_state** | **str**| trace state |

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

# **get_app_qos_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_qos_data(trace_id, timestamp, received_timestamp)



Get QoS Application data for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    received_timestamp = 1 # int | received timestamp

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_qos_data(trace_id, timestamp, received_timestamp)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_app_qos_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **received_timestamp** | **int**| received timestamp |

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

# **get_app_qos_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_qos_state(trace_id, timestamp, trace_state)



Get QoS Application state to received timestamp mapping for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    trace_state = "traceState_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_qos_state(trace_id, timestamp, trace_state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_app_qos_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **trace_state** | **str**| trace state |

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

# **get_concurrent_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_concurrent_data(trace_id, timestamp)



Get concurrent data for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_concurrent_data(trace_id, timestamp)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_concurrent_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_concurrent_domain_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_concurrent_domain_data(trace_id, timestamp)



Get concurrent domain data for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_concurrent_domain_data(trace_id, timestamp)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_concurrent_domain_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_event_app_hop_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_event_app_hop_list(trace_id, timestamp, state)



Get Trace Application and HopList for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    state = "state_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_event_app_hop_list(trace_id, timestamp, state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_event_app_hop_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **state** | **str**| trace state |

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

# **get_event_app_score_bandwidth**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_event_app_score_bandwidth(trace_id, timestamp, state, received_timestamp)



Get Trace Event Application Performance Score and Bandwidth for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    state = "state_example" # str | trace state
    received_timestamp = 1 # int | received timestamp

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_event_app_score_bandwidth(trace_id, timestamp, state, received_timestamp)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_event_app_score_bandwidth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **state** | **str**| trace state |
 **received_timestamp** | **int**| received timestamp |

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

# **get_event_flow_from_app_hop**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_event_flow_from_app_hop(trace_id, timestamp, state, application, direction, _from, to, device_trace_id)



Get Trace Event Flow From Application And Hop for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    state = "state_example" # str | trace state
    application = "application_example" # str | app name
    direction = "direction_example" # str | direction
    _from = "from_example" # str | from
    to = "to_example" # str | to
    device_trace_id = 1 # int | deviceTraceId

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_event_flow_from_app_hop(trace_id, timestamp, state, application, direction, _from, to, device_trace_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_event_flow_from_app_hop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **state** | **str**| trace state |
 **application** | **str**| app name |
 **direction** | **str**| direction |
 **_from** | **str**| from |
 **to** | **str**| to |
 **device_trace_id** | **int**| deviceTraceId |

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

# **get_event_readout**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_event_readout(trace_id, timestamp, state)



Get Trace Event Readout for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    state = "state_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_event_readout(trace_id, timestamp, state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_event_readout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **state** | **str**| trace state |

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

# **get_routing_detail_from_local**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_routing_detail_from_local(trace_id, timestamp, trace_state, route_prefixs)



Get Routing Details for NWPI.

### Example


```python
import time
import openapi_client
from openapi_client.api import nwpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nwpi_api.NWPIApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    trace_state = "traceState_example" # str | trace state
    route_prefixs = "routePrefixs_example" # str | route prefixs

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_detail_from_local(trace_id, timestamp, trace_state, route_prefixs)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NWPIApi->get_routing_detail_from_local: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **trace_state** | **str**| trace state |
 **route_prefixs** | **str**| route prefixs |

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

