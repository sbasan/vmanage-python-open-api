# openapi_client.MonitoringCellularEIOLTEApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregation_data_by_query7**](MonitoringCellularEIOLTEApi.md#get_aggregation_data_by_query7) | **GET** /statistics/eiolte/aggregation | 
[**get_count9**](MonitoringCellularEIOLTEApi.md#get_count9) | **GET** /statistics/eiolte/doccount | 
[**get_count_post9**](MonitoringCellularEIOLTEApi.md#get_count_post9) | **POST** /statistics/eiolte/doccount | 
[**get_post_aggregation_app_data_by_query7**](MonitoringCellularEIOLTEApi.md#get_post_aggregation_app_data_by_query7) | **POST** /statistics/eiolte/app-agg/aggregation | 
[**get_post_aggregation_data_by_query7**](MonitoringCellularEIOLTEApi.md#get_post_aggregation_data_by_query7) | **POST** /statistics/eiolte/aggregation | 
[**get_post_stat_bulk_raw_data7**](MonitoringCellularEIOLTEApi.md#get_post_stat_bulk_raw_data7) | **POST** /statistics/eiolte/page | 
[**get_stat_bulk_raw_data7**](MonitoringCellularEIOLTEApi.md#get_stat_bulk_raw_data7) | **GET** /statistics/eiolte/page | 
[**get_stat_data_fields9**](MonitoringCellularEIOLTEApi.md#get_stat_data_fields9) | **GET** /statistics/eiolte/fields | 
[**get_stat_data_raw_data7**](MonitoringCellularEIOLTEApi.md#get_stat_data_raw_data7) | **GET** /statistics/eiolte | 
[**get_stat_data_raw_data_as_csv7**](MonitoringCellularEIOLTEApi.md#get_stat_data_raw_data_as_csv7) | **GET** /statistics/eiolte/csv | 
[**get_stat_query_fields9**](MonitoringCellularEIOLTEApi.md#get_stat_query_fields9) | **GET** /statistics/eiolte/query/fields | 
[**get_stats_raw_data7**](MonitoringCellularEIOLTEApi.md#get_stats_raw_data7) | **POST** /statistics/eiolte | 


# **get_aggregation_data_by_query7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query7()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query7(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_aggregation_data_by_query7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]

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

# **get_count9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count9(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2021-05-10T01:00:00 UTC","2021-11-30T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count9(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_count9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

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

# **get_count_post9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post9()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post9(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_count_post9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query | [optional]

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

# **get_post_aggregation_app_data_by_query7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query7()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query7(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_post_aggregation_app_data_by_query7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_aggregation_data_by_query7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query7()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query7(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_post_aggregation_data_by_query7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_stat_bulk_raw_data7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data7()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data7(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_post_stat_bulk_raw_data7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_stat_bulk_raw_data7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data7()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data7(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stat_bulk_raw_data7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]

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

# **get_stat_data_fields9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields9()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields9()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stat_data_fields9: %s\n" % e)
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

# **get_stat_data_raw_data7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data7()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by(emp:entry_time) (optional)
    sort_order = "sortOrder_example" # str | sort order(emp:asc、ASC、Asc、desc、Desc、DESC) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data7(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stat_data_raw_data7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by(emp:entry_time) | [optional]
 **sort_order** | **str**| sort order(emp:asc、ASC、Asc、desc、Desc、DESC) | [optional]

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

# **get_stat_data_raw_data_as_csv7**
> str get_stat_data_raw_data_as_csv7()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv7(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stat_data_raw_data_as_csv7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_query_fields9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields9()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields9()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stat_query_fields9: %s\n" % e)
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

# **get_stats_raw_data7**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data7()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cellular_eiolte_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cellular_eiolte_api.MonitoringCellularEIOLTEApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data7(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCellularEIOLTEApi->get_stats_raw_data7: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

