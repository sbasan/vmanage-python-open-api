# openapi_client.ToolsTACCasesApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_call**](ToolsTACCasesApi.md#delete_call) | **DELETE** /opentaccase/scmwidget | 
[**get_call**](ToolsTACCasesApi.md#get_call) | **GET** /opentaccase/scmwidget | 
[**get_client_id**](ToolsTACCasesApi.md#get_client_id) | **GET** /opentaccase/getClientID | 
[**oauth_access**](ToolsTACCasesApi.md#oauth_access) | **GET** /opentaccase/authcode | 
[**post_call**](ToolsTACCasesApi.md#post_call) | **POST** /opentaccase/scmwidget | 


# **delete_call**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] delete_call()



Proxy API for SCM Widget

### Example


```python
import time
import openapi_client
from openapi_client.api import tools_tac_cases_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tools_tac_cases_api.ToolsTACCasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_call()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ToolsTACCasesApi->delete_call: %s\n" % e)
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

# **get_call**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_call()



Proxy API for SCM Widget

### Example


```python
import time
import openapi_client
from openapi_client.api import tools_tac_cases_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tools_tac_cases_api.ToolsTACCasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_call()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ToolsTACCasesApi->get_call: %s\n" % e)
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

# **get_client_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_client_id()



Gets vManage Client ID

### Example


```python
import time
import openapi_client
from openapi_client.api import tools_tac_cases_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tools_tac_cases_api.ToolsTACCasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_client_id()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ToolsTACCasesApi->get_client_id: %s\n" % e)
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

# **oauth_access**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] oauth_access()



Gets Access Token for SSO Logjn

### Example


```python
import time
import openapi_client
from openapi_client.api import tools_tac_cases_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tools_tac_cases_api.ToolsTACCasesApi(api_client)
    code = "code_example" # str |  (optional)
    redirect = "redirect_example" # str |  (optional)
    is_refresh_needed = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.oauth_access(code=code, redirect=redirect, is_refresh_needed=is_refresh_needed)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ToolsTACCasesApi->oauth_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional]
 **redirect** | **str**|  | [optional]
 **is_refresh_needed** | **bool**|  | [optional]

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

# **post_call**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] post_call()



Prxoy API for SCM Widget

### Example


```python
import time
import openapi_client
from openapi_client.api import tools_tac_cases_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tools_tac_cases_api.ToolsTACCasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_call()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ToolsTACCasesApi->post_call: %s\n" % e)
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

