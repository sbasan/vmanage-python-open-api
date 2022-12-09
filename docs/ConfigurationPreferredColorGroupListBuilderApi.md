# openapi_client.ConfigurationPreferredColorGroupListBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_list28**](ConfigurationPreferredColorGroupListBuilderApi.md#create_policy_list28) | **POST** /template/policy/list/preferredcolorgroup | 
[**delete_policy_list28**](ConfigurationPreferredColorGroupListBuilderApi.md#delete_policy_list28) | **DELETE** /template/policy/list/preferredcolorgroup/{id} | 
[**delete_policy_lists_with_info_tag28**](ConfigurationPreferredColorGroupListBuilderApi.md#delete_policy_lists_with_info_tag28) | **DELETE** /template/policy/list/preferredcolorgroup | 
[**edit_policy_list28**](ConfigurationPreferredColorGroupListBuilderApi.md#edit_policy_list28) | **PUT** /template/policy/list/preferredcolorgroup/{id} | 
[**get_lists_by_id28**](ConfigurationPreferredColorGroupListBuilderApi.md#get_lists_by_id28) | **GET** /template/policy/list/preferredcolorgroup/{id} | 
[**get_policy_lists25**](ConfigurationPreferredColorGroupListBuilderApi.md#get_policy_lists25) | **GET** /template/policy/list/preferredcolorgroup | 
[**get_policy_lists_with_info_tag28**](ConfigurationPreferredColorGroupListBuilderApi.md#get_policy_lists_with_info_tag28) | **GET** /template/policy/list/preferredcolorgroup/filtered | 
[**preview_policy_list28**](ConfigurationPreferredColorGroupListBuilderApi.md#preview_policy_list28) | **POST** /template/policy/list/preferredcolorgroup/preview | 
[**preview_policy_list_by_id28**](ConfigurationPreferredColorGroupListBuilderApi.md#preview_policy_list_by_id28) | **GET** /template/policy/list/preferredcolorgroup/preview/{id} | 


# **create_policy_list28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_policy_list28()



Create policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_policy_list28(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->create_policy_list28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **delete_policy_list28**
> delete_policy_list28(id)



Delete policy list entry for a specific type of policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_policy_list28(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->delete_policy_list28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **delete_policy_lists_with_info_tag28**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] delete_policy_lists_with_info_tag28()



Delete policy lists with specific info tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    info_tag = "infoTag_example" # str | InfoTag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_policy_lists_with_info_tag28(info_tag=info_tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->delete_policy_lists_with_info_tag28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_tag** | **str**| InfoTag | [optional]

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

# **edit_policy_list28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_policy_list28(id)



Edit policy list entries for a specific type of policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_policy_list28(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->edit_policy_list28: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_policy_list28(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->edit_policy_list28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **get_lists_by_id28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_lists_by_id28(id)



Get a specific policy list based on the id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lists_by_id28(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->get_lists_by_id28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **get_policy_lists25**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_policy_lists25()



Get policy lists

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_policy_lists25()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->get_policy_lists25: %s\n" % e)
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

# **get_policy_lists_with_info_tag28**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_policy_lists_with_info_tag28()



Get policy lists with specific info tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    info_tag = "infoTag_example" # str | InfoTag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_policy_lists_with_info_tag28(info_tag=info_tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->get_policy_lists_with_info_tag28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_tag** | **str**| InfoTag | [optional]

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

# **preview_policy_list28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_list28()



Preview a policy list based on the policy list type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_policy_list28(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->preview_policy_list28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **preview_policy_list_by_id28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_list_by_id28(id)



Preview a specific policy list entry based on id provided

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_preferred_color_group_list_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_preferred_color_group_list_builder_api.ConfigurationPreferredColorGroupListBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_policy_list_by_id28(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreferredColorGroupListBuilderApi->preview_policy_list_by_id28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

