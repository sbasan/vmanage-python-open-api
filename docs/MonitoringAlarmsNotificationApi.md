# openapi_client.MonitoringAlarmsNotificationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_rule**](MonitoringAlarmsNotificationApi.md#create_notification_rule) | **POST** /notifications/rule | 
[**delete_notification_rule**](MonitoringAlarmsNotificationApi.md#delete_notification_rule) | **DELETE** /notifications/rules | 
[**get_notification_rule**](MonitoringAlarmsNotificationApi.md#get_notification_rule) | **GET** /notifications/rules | 
[**update_notification_rule**](MonitoringAlarmsNotificationApi.md#update_notification_rule) | **PUT** /notifications/rule | 


# **create_notification_rule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_notification_rule()



Add notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_notification_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_notification_api.MonitoringAlarmsNotificationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Notification rule (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_notification_rule(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsNotificationApi->create_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Notification rule | [optional]

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_rule**
> delete_notification_rule(rule_id)



Delete notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_notification_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_notification_api.MonitoringAlarmsNotificationApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_notification_rule(rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsNotificationApi->delete_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id |

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

# **get_notification_rule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_notification_rule()



Get all rules or specific notification rule by its Id

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_notification_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_notification_api.MonitoringAlarmsNotificationApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_notification_rule(rule_id=rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsNotificationApi->get_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id | [optional]

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

# **update_notification_rule**
> update_notification_rule(rule_id)



Update notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_notification_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_notification_api.MonitoringAlarmsNotificationApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Notification rule (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_notification_rule(rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsNotificationApi->update_notification_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_notification_rule(rule_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsNotificationApi->update_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Notification rule | [optional]

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

