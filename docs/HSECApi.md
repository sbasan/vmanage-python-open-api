# openapi_client.HSECApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_slac**](HSECApi.md#assign_slac) | **POST** /hsec/assignSlac | 
[**device_summmary**](HSECApi.md#device_summmary) | **GET** /hsec/devices | 
[**device_summmary1**](HSECApi.md#device_summmary1) | **GET** /hsec/devices/install | 
[**download_slac_request_file**](HSECApi.md#download_slac_request_file) | **POST** /hsec/download | 
[**fetch_accounts1**](HSECApi.md#fetch_accounts1) | **GET** /hsec/fetchaccounts | 
[**upload_slac_file**](HSECApi.md#upload_slac_file) | **POST** /hsec/uploadAuth | 


# **assign_slac**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} assign_slac()



Assign Hsec License to devices from uploaded SLAC file

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)
    data = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.assign_slac(data=data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->assign_slac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **file_type**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_summmary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} device_summmary()



Give list of HSEC license devices

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.device_summmary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->device_summmary: %s\n" % e)
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

# **device_summmary1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} device_summmary1()



Give list of HSEC license devices

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.device_summmary1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->device_summmary1: %s\n" % e)
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

# **download_slac_request_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_slac_request_file()



Download SLAC Request file for CSSM

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device List (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.download_slac_request_file(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->download_slac_request_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device List | [optional]

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

# **fetch_accounts1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_accounts1(username, pwd, mode)



fetch sava accounts that support HSEC Licensing

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)
    username = "username_example" # str | userName
    pwd = "pwd_example" # str | password
    mode = "mode_example" # str | mode

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_accounts1(username, pwd, mode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->fetch_accounts1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| userName |
 **pwd** | **str**| password |
 **mode** | **str**| mode |

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

# **upload_slac_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_slac_file()



upload SLAC File and fetch device summary

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_api.HSECApi(api_client)
    data = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.upload_slac_file(data=data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECApi->upload_slac_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **file_type**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

