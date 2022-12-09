# openapi_client.SystemReverseProxyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reverse_proxy_mappings**](SystemReverseProxyApi.md#create_reverse_proxy_mappings) | **POST** /system/reverseproxy/{uuid} | 
[**get_reverse_proxy_mappings**](SystemReverseProxyApi.md#get_reverse_proxy_mappings) | **GET** /system/reverseproxy/{uuid} | 


# **create_reverse_proxy_mappings**
> create_reverse_proxy_mappings(uuid)



Create reverse proxy IP/Port mappings for controller

### Example


```python
import time
import openapi_client
from openapi_client.api import system_reverse_proxy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_reverse_proxy_api.SystemReverseProxyApi(api_client)
    uuid = "uuid_example" # str | Device uuid
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device reverse proxy mappings (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_reverse_proxy_mappings(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemReverseProxyApi->create_reverse_proxy_mappings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_reverse_proxy_mappings(uuid, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemReverseProxyApi->create_reverse_proxy_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device reverse proxy mappings | [optional]

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

# **get_reverse_proxy_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_reverse_proxy_mappings(uuid)



Get reverse proxy IP/Port mappings for controller

### Example


```python
import time
import openapi_client
from openapi_client.api import system_reverse_proxy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_reverse_proxy_api.SystemReverseProxyApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_reverse_proxy_mappings(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemReverseProxyApi->get_reverse_proxy_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

