# openapi_client.HsecActivateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_hsec_licenses**](HsecActivateApi.md#activate_hsec_licenses) | **POST** /hsec/activate | 


# **activate_hsec_licenses**
> activate_hsec_licenses()



Activate Hsec licenses on devices

### Example


```python
import time
import openapi_client
from openapi_client.api import hsec_activate_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hsec_activate_api.HsecActivateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant List (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.activate_hsec_licenses(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling HsecActivateApi->activate_hsec_licenses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant List | [optional]

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

