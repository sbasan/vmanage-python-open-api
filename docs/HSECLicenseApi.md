# openapi_client.HSECLicenseApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hsecassign**](HSECLicenseApi.md#hsecassign) | **POST** /hsec/assign | 


# **hsecassign**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} hsecassign()



hsec 

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_license_api.HSECLicenseApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.hsecassign(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HSECLicenseApi->hsecassign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

