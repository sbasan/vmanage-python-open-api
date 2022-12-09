# openapi_client.ConfigurationIseServerApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_activate**](ConfigurationIseServerApi.md#account_activate) | **POST** /ise/pxgrid/activate | 
[**account_create**](ConfigurationIseServerApi.md#account_create) | **POST** /ise/pxgrid/create | 
[**add_ise_server_credentials**](ConfigurationIseServerApi.md#add_ise_server_credentials) | **POST** /ise/credentials | 
[**approve**](ConfigurationIseServerApi.md#approve) | **PUT** /ise/pxgrid/approve | 
[**connect1**](ConfigurationIseServerApi.md#connect1) | **GET** /ise/connect | 
[**delete_ise_and_px_grid_account**](ConfigurationIseServerApi.md#delete_ise_and_px_grid_account) | **DELETE** /ise/credentials/iseandpxgrid | 
[**delete_px_grid**](ConfigurationIseServerApi.md#delete_px_grid) | **DELETE** /ise/credentials/pxgrid | 
[**get_identity_user_groups**](ConfigurationIseServerApi.md#get_identity_user_groups) | **POST** /template/policy/ise/identity/usergroups | 
[**get_identity_users**](ConfigurationIseServerApi.md#get_identity_users) | **POST** /template/policy/ise/identity/users | 
[**get_ise_server_credentials**](ConfigurationIseServerApi.md#get_ise_server_credentials) | **GET** /ise/credentials | 
[**get_p_xgrid_cert**](ConfigurationIseServerApi.md#get_p_xgrid_cert) | **GET** /ise/credentials/pxgrid/cert | 
[**get_px_grid_account**](ConfigurationIseServerApi.md#get_px_grid_account) | **GET** /ise/credentials/pxgrid | 
[**sync_vsmart**](ConfigurationIseServerApi.md#sync_vsmart) | **POST** /ise/credentials/vsmart/sync | 
[**update_ise_server_credentials**](ConfigurationIseServerApi.md#update_ise_server_credentials) | **PUT** /ise/credentials | 


# **account_activate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} account_activate()



pxGrid Account Activate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.account_activate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->account_activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **account_create**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} account_create()



pxGrid Account Create

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.account_create(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->account_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **add_ise_server_credentials**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_ise_server_credentials()



Add Ise server credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Config Ise server request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_ise_server_credentials(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->add_ise_server_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Config Ise server request | [optional]

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

# **approve**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} approve()



pxGrid Account Approve with ERS API

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.approve()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->approve: %s\n" % e)
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

# **connect1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} connect1()



ISE connect

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.connect1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->connect1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ise_and_px_grid_account**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_ise_and_px_grid_account()



Delete ISE and PxGrid on vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_ise_and_px_grid_account()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->delete_ise_and_px_grid_account: %s\n" % e)
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

# **delete_px_grid**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_px_grid()



Delete PxGrid on vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_px_grid()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->delete_px_grid: %s\n" % e)
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

# **get_identity_user_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_identity_user_groups()



Get all identity user groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Get Users (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_identity_user_groups(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->get_identity_user_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Get Users | [optional]

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

# **get_identity_users**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_identity_users()



Get all identity users

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Get Users (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_identity_users(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->get_identity_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Get Users | [optional]

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

# **get_ise_server_credentials**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ise_server_credentials()



Get Ise server credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_ise_server_credentials()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->get_ise_server_credentials: %s\n" % e)
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

# **get_p_xgrid_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_p_xgrid_cert()



getPXgridCert

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_p_xgrid_cert()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->get_p_xgrid_cert: %s\n" % e)
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

# **get_px_grid_account**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_px_grid_account()



Get PXGrid account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_px_grid_account()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->get_px_grid_account: %s\n" % e)
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

# **sync_vsmart**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_vsmart()



syncVsmart

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.sync_vsmart()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->sync_vsmart: %s\n" % e)
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

# **update_ise_server_credentials**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_ise_server_credentials()



Configure Ise server credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_ise_server_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_ise_server_api.ConfigurationIseServerApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Config Ise server request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_ise_server_credentials(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationIseServerApi->update_ise_server_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Config Ise server request | [optional]

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

