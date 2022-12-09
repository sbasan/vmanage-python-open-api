# openapi_client.ColocationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acitvate_cloud_dock_cluster**](ColocationApi.md#acitvate_cloud_dock_cluster) | **POST** /colocation/cluster/activate | 
[**attach_service_chain**](ColocationApi.md#attach_service_chain) | **POST** /colocation/servicechain/attach | 
[**attach_service_chain1**](ColocationApi.md#attach_service_chain1) | **POST** /colocation/servicechain/autoattach | 
[**cancel_button**](ColocationApi.md#cancel_button) | **POST** /colocation/servicechain/cancel | 
[**cloud_dock_cluster_preview**](ColocationApi.md#cloud_dock_cluster_preview) | **GET** /colocation/cluster/config | 
[**create_cloud_dock_cluster**](ColocationApi.md#create_cloud_dock_cluster) | **POST** /colocation/cluster | 
[**de_acitvate_cloud_dock_cluster**](ColocationApi.md#de_acitvate_cloud_dock_cluster) | **POST** /colocation/cluster/deactivate | 
[**delete_cloud_dock_cluster_by_name**](ColocationApi.md#delete_cloud_dock_cluster_by_name) | **DELETE** /colocation/cluster/{clustername} | 
[**detach_service_chain**](ColocationApi.md#detach_service_chain) | **PUT** /colocation/servicechain/detach | 
[**dummyccm**](ColocationApi.md#dummyccm) | **GET** /colocation/cluster/activateClusterDummy | 
[**dummycsp_state**](ColocationApi.md#dummycsp_state) | **GET** /colocation/cluster/activateClusterDummyState | 
[**get_cloud_dock_cluster_detail**](ColocationApi.md#get_cloud_dock_cluster_detail) | **GET** /colocation/cluster | 
[**get_cloud_dock_cluster_detail_by_id**](ColocationApi.md#get_cloud_dock_cluster_detail_by_id) | **GET** /colocation/cluster/id | 
[**get_cluster_config_by_cluster_id**](ColocationApi.md#get_cluster_config_by_cluster_id) | **GET** /colocation/monitor/cluster/config | 
[**get_cluster_details_by_cluster_id**](ColocationApi.md#get_cluster_details_by_cluster_id) | **GET** /colocation/monitor/cluster | 
[**get_cluster_port_mapping_by_cluster_id**](ColocationApi.md#get_cluster_port_mapping_by_cluster_id) | **GET** /colocation/monitor/cluster/portView | 
[**get_device_detail_by_device_id**](ColocationApi.md#get_device_detail_by_device_id) | **GET** /colocation/monitor/device | 
[**get_edge_devices**](ColocationApi.md#get_edge_devices) | **GET** /colocation/servicechain/edge/devices | 
[**get_pnf_config**](ColocationApi.md#get_pnf_config) | **GET** /colocation/monitor/pnf/configuration | 
[**get_service_chain_details**](ColocationApi.md#get_service_chain_details) | **GET** /colocation/monitor/servicechain | 
[**get_service_group_by_cluster_id**](ColocationApi.md#get_service_group_by_cluster_id) | **GET** /colocation/monitor/servicegroup | 
[**get_system_status_by_device_id**](ColocationApi.md#get_system_status_by_device_id) | **GET** /colocation/monitor/device/system | 
[**get_vnf_alarm_count**](ColocationApi.md#get_vnf_alarm_count) | **GET** /colocation/monitor/vnf/alarms/count | 
[**get_vnf_events_count_detail**](ColocationApi.md#get_vnf_events_count_detail) | **GET** /colocation/monitor/vnf/alarms | 
[**get_vnf_events_detail**](ColocationApi.md#get_vnf_events_detail) | **GET** /colocation/monitor/vnf/events | 
[**get_vnf_interface_detail**](ColocationApi.md#get_vnf_interface_detail) | **GET** /colocation/monitor/vnf/interface | 
[**getpnf_details**](ColocationApi.md#getpnf_details) | **GET** /colocation/monitor/pnf | 
[**getpnf_devices**](ColocationApi.md#getpnf_devices) | **GET** /colocation/servicechain/edge/pnfdevices | 
[**getvnf_by_device_id**](ColocationApi.md#getvnf_by_device_id) | **GET** /colocation/monitor/device/vnf | 
[**getvnf_details**](ColocationApi.md#getvnf_details) | **GET** /colocation/monitor/vnf | 
[**list_network_function_map**](ColocationApi.md#list_network_function_map) | **GET** /colocation/monitor/networkfunction/listmap | 
[**rma_cloud_dock_csp**](ColocationApi.md#rma_cloud_dock_csp) | **POST** /colocation/cluster/rma | 
[**update_cloud_dock_cluster**](ColocationApi.md#update_cloud_dock_cluster) | **PUT** /colocation/cluster | 
[**update_csp_to_cluster**](ColocationApi.md#update_csp_to_cluster) | **PUT** /colocation/cluster/attached/csp | 
[**vnf_actions**](ColocationApi.md#vnf_actions) | **POST** /colocation/monitor/vnf/action | 


# **acitvate_cloud_dock_cluster**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} acitvate_cloud_dock_cluster(cluster_name)



Activate a cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.acitvate_cloud_dock_cluster(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->acitvate_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

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

# **attach_service_chain**
> attach_service_chain()



Attach service chain to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Attach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.attach_service_chain(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->attach_service_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Attach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_service_chain1**
> attach_service_chain1()



Attach service chain to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Attach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.attach_service_chain1(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->attach_service_chain1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Attach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_button**
> cancel_button()



Cancel button to cancel configuring devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cancel configuring devices (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cancel_button(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->cancel_button: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cancel configuring devices | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloud_dock_cluster_preview**
> str cloud_dock_cluster_preview(serial_number)



Clouddock cluster preview

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    serial_number = "serialNumber_example" # str | Serial number

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cloud_dock_cluster_preview(serial_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->cloud_dock_cluster_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Serial number |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_dock_cluster**
> create_cloud_dock_cluster()



Add a new cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_cloud_dock_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->create_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cluster config | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **de_acitvate_cloud_dock_cluster**
> de_acitvate_cloud_dock_cluster(cluster_id)



Deactivate clouddock cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.de_acitvate_cloud_dock_cluster(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->de_acitvate_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_dock_cluster_by_name**
> delete_cloud_dock_cluster_by_name(clustername)



Delete cluster by name

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    clustername = "clustername_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cloud_dock_cluster_by_name(clustername)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->delete_cloud_dock_cluster_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustername** | **str**| Cluster name |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_service_chain**
> detach_service_chain()



Detach service chain

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Detach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.detach_service_chain(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->detach_service_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Detach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dummyccm**
> dummyccm(cluster_name)



Activate dummp cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_instance.dummyccm(cluster_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->dummyccm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dummycsp_state**
> dummycsp_state(cluster_name, state)



Activate cluster in a state

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name
    state = "state_example" # str | Cluster state

    # example passing only required values which don't have defaults set
    try:
        api_instance.dummycsp_state(cluster_name, state)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->dummycsp_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |
 **state** | **str**| Cluster state |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_dock_cluster_detail**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_dock_cluster_detail(cluster_name)



Get details of all existing Clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_cluster_detail(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_cloud_dock_cluster_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |

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

# **get_cloud_dock_cluster_detail_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_dock_cluster_detail_by_id(cluster_id)



Get cluster by Id

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_cluster_detail_by_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_cloud_dock_cluster_detail_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_cluster_config_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cluster_config_by_cluster_id(cluster_id)



Provide details of devices of clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_config_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_cluster_config_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_cluster_details_by_cluster_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cluster_details_by_cluster_id(cluster_id)



Provide details of ids of existing clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_details_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_cluster_details_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_cluster_port_mapping_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cluster_port_mapping_by_cluster_id(cluster_id)



Provide details of port mappings in the cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_port_mapping_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_cluster_port_mapping_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_device_detail_by_device_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_detail_by_device_id()



List details for Device

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_detail_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_device_detail_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **get_edge_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_edge_devices()



Get edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_edge_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_edge_devices: %s\n" % e)
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

# **get_pnf_config**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_pnf_config()



List configuration of PNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    pnf_serial_number = "pnfSerialNumber_example" # str | PNF serial number (optional)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_pnf_config(pnf_serial_number=pnf_serial_number, cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_pnf_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnf_serial_number** | **str**| PNF serial number | [optional]
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **get_service_chain_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_service_chain_details()



List all service chain or service chains by Id

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)
    user_group_name = "userGroupName_example" # str | UserGroup Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_chain_details(cluster_id=cluster_id, user_group_name=user_group_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_service_chain_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]
 **user_group_name** | **str**| UserGroup Name | [optional]

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

# **get_service_group_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_service_group_by_cluster_id()



List all attached serviceGroups to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_group_by_cluster_id(cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_service_group_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **get_system_status_by_device_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_system_status_by_device_id()



List all connected VNF to a device

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_system_status_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_system_status_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **get_vnf_alarm_count**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_alarm_count()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    user_group = "user_group_example" # str | user group name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_alarm_count(user_group=user_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_vnf_alarm_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**| user group name | [optional]

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

# **get_vnf_events_count_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_events_count_detail()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    user_group = "user_group_example" # str | user group name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_events_count_detail(user_group=user_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_vnf_events_count_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**| user group name | [optional]

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

# **get_vnf_events_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_events_detail()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    vnf_name = "vnfName_example" # str | VNF name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_events_detail(vnf_name=vnf_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_vnf_events_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnf_name** | **str**| VNF name | [optional]

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

# **get_vnf_interface_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_interface_detail()



Get interface detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    vnf_name = "vnfName_example" # str | VNF name (optional)
    device_ip = "deviceIp_example" # str | Device IP (optional)
    device_class = "deviceClass_example" # str | Device class (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_interface_detail(vnf_name=vnf_name, device_ip=device_ip, device_class=device_class)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->get_vnf_interface_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnf_name** | **str**| VNF name | [optional]
 **device_ip** | **str**| Device IP | [optional]
 **device_class** | **str**| Device class | [optional]

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

# **getpnf_details**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getpnf_details()



List all PNF by cluster Id

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getpnf_details(cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->getpnf_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **getpnf_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getpnf_devices(pnf_device_type)



Get PNF edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    pnf_device_type = "pnfDeviceType_example" # str | PNF device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.getpnf_devices(pnf_device_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->getpnf_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnf_device_type** | **str**| PNF device type |

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

# **getvnf_by_device_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getvnf_by_device_id()



List all VNF attached with Device

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getvnf_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->getvnf_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **getvnf_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getvnf_details()



Provide details of all existing VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)
    user_group_name = "userGroupName_example" # str | UserGroup Name (optional)
    vnf_name = "vnfName_example" # str | VNF Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getvnf_details(cluster_id=cluster_id, user_group_name=user_group_name, vnf_name=vnf_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->getvnf_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]
 **user_group_name** | **str**| UserGroup Name | [optional]
 **vnf_name** | **str**| VNF Name | [optional]

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

# **list_network_function_map**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_network_function_map()



Retrieve network function listing

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_network_function_map()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->list_network_function_map: %s\n" % e)
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

# **rma_cloud_dock_csp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} rma_cloud_dock_csp(cluster_name)



RMA operation for CSP device

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    cluster_name = "clusterName_example" # str | Cluster name
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rma_cloud_dock_csp(cluster_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->rma_cloud_dock_csp: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.rma_cloud_dock_csp(cluster_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->rma_cloud_dock_csp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name |
 **body** | **str**|  | [optional]

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

# **update_cloud_dock_cluster**
> update_cloud_dock_cluster()



Update a existing cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_cloud_dock_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->update_cloud_dock_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cluster config | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_csp_to_cluster**
> update_csp_to_cluster()



Update attached csp to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSP config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_csp_to_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->update_csp_to_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSP config | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf_actions**
> vnf_actions()



VNF action

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_api.ColocationApi(api_client)
    vm_name = "vmName_example" # str | VM Name (optional)
    device_id = "deviceId_example" # str | Device Id (optional)
    action = "action_example" # str | Action (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.vnf_actions(vm_name=vm_name, device_id=device_id, action=action)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationApi->vnf_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_name** | **str**| VM Name | [optional]
 **device_id** | **str**| Device Id | [optional]
 **action** | **str**| Action | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

