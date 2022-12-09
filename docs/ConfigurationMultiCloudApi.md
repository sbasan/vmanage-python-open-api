# openapi_client.ConfigurationMultiCloudApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_edge_global_settings**](ConfigurationMultiCloudApi.md#add_edge_global_settings) | **POST** /multicloud/settings/edge/global | 
[**add_global_settings**](ConfigurationMultiCloudApi.md#add_global_settings) | **POST** /multicloud/settings/global | 
[**attach_sites**](ConfigurationMultiCloudApi.md#attach_sites) | **POST** /multicloud/cloudgateway/{cloudGatewayName}/site | 
[**audit**](ConfigurationMultiCloudApi.md#audit) | **POST** /multicloud/audit | 
[**audit_dry_run**](ConfigurationMultiCloudApi.md#audit_dry_run) | **GET** /multicloud/audit | 
[**clean_up_all_connectivity_gateways_in_local_db**](ConfigurationMultiCloudApi.md#clean_up_all_connectivity_gateways_in_local_db) | **DELETE** /multicloud/connectivitygateway | 
[**create_cgw**](ConfigurationMultiCloudApi.md#create_cgw) | **POST** /multicloud/cloudgateway | 
[**create_connectivity_gateway**](ConfigurationMultiCloudApi.md#create_connectivity_gateway) | **POST** /multicloud/connectivitygateway | 
[**create_device_link**](ConfigurationMultiCloudApi.md#create_device_link) | **POST** /multicloud/devicelink/edge | 
[**create_edge_connectivity**](ConfigurationMultiCloudApi.md#create_edge_connectivity) | **POST** /multicloud/connectivity/edge | 
[**create_icgw**](ConfigurationMultiCloudApi.md#create_icgw) | **POST** /multicloud/gateway/edge | 
[**create_virtual_wan**](ConfigurationMultiCloudApi.md#create_virtual_wan) | **POST** /multicloud/vwan | 
[**delete_account**](ConfigurationMultiCloudApi.md#delete_account) | **DELETE** /multicloud/accounts/{accountId} | 
[**delete_cgw**](ConfigurationMultiCloudApi.md#delete_cgw) | **DELETE** /multicloud/cloudgateway/{cloudGatewayName} | 
[**delete_connectivity_gateway**](ConfigurationMultiCloudApi.md#delete_connectivity_gateway) | **DELETE** /multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName} | 
[**delete_device_link**](ConfigurationMultiCloudApi.md#delete_device_link) | **DELETE** /multicloud/devicelink/edge/{deviceLinkName} | 
[**delete_edge_account**](ConfigurationMultiCloudApi.md#delete_edge_account) | **DELETE** /multicloud/accounts/edge/{accountId} | 
[**delete_edge_account1**](ConfigurationMultiCloudApi.md#delete_edge_account1) | **DELETE** /multicloud/locations/edge/{edgeType} | 
[**delete_edge_connectivity**](ConfigurationMultiCloudApi.md#delete_edge_connectivity) | **DELETE** /multicloud/connectivity/edge/{connectionName} | 
[**delete_icgw**](ConfigurationMultiCloudApi.md#delete_icgw) | **DELETE** /multicloud/gateway/edge/{edgeGatewayName} | 
[**delete_virtual_wan**](ConfigurationMultiCloudApi.md#delete_virtual_wan) | **DELETE** /multicloud/vwan/{cloudProvider}/{vWanName} | 
[**detach_sites1**](ConfigurationMultiCloudApi.md#detach_sites1) | **DELETE** /multicloud/cloudgateway/{cloudGatewayName}/site | 
[**edge_audit**](ConfigurationMultiCloudApi.md#edge_audit) | **POST** /multicloud/audit/edge | 
[**edge_audit_dry_run**](ConfigurationMultiCloudApi.md#edge_audit_dry_run) | **GET** /multicloud/audit/edge | 
[**edit_tag**](ConfigurationMultiCloudApi.md#edit_tag) | **PUT** /multicloud/hostvpc/tags | 
[**get_all_cloud_accounts**](ConfigurationMultiCloudApi.md#get_all_cloud_accounts) | **GET** /multicloud/accounts | 
[**get_azure_network_virtual_appliances**](ConfigurationMultiCloudApi.md#get_azure_network_virtual_appliances) | **GET** /multicloud/cloudgateway/nvas | 
[**get_azure_nva_sku_list**](ConfigurationMultiCloudApi.md#get_azure_nva_sku_list) | **GET** /multicloud/cloudgateway/nvasku | 
[**get_azure_resource_groups**](ConfigurationMultiCloudApi.md#get_azure_resource_groups) | **GET** /multicloud/cloudgateway/resourceGroups | 
[**get_azure_virtual_hubs**](ConfigurationMultiCloudApi.md#get_azure_virtual_hubs) | **GET** /multicloud/cloudgateway/vhubs | 
[**get_azure_virtual_wans**](ConfigurationMultiCloudApi.md#get_azure_virtual_wans) | **GET** /multicloud/cloudgateway/vwans | 
[**get_cgw_associated_mappings**](ConfigurationMultiCloudApi.md#get_cgw_associated_mappings) | **GET** /multicloud/mapping/{cloudType} | 
[**get_cgw_custom_setting_details**](ConfigurationMultiCloudApi.md#get_cgw_custom_setting_details) | **GET** /multicloud/cloudgatewaysetting/{cloudGatewayName} | 
[**get_cgw_details**](ConfigurationMultiCloudApi.md#get_cgw_details) | **GET** /multicloud/cloudgateway/{cloudGatewayName} | 
[**get_cgw_org_resources**](ConfigurationMultiCloudApi.md#get_cgw_org_resources) | **GET** /multicloud/cloudgateway/resource | 
[**get_cgw_types**](ConfigurationMultiCloudApi.md#get_cgw_types) | **GET** /multicloud/cloudgatewaytype | 
[**get_cgws**](ConfigurationMultiCloudApi.md#get_cgws) | **GET** /multicloud/cloudgateway | 
[**get_cloud_account_details**](ConfigurationMultiCloudApi.md#get_cloud_account_details) | **GET** /multicloud/accounts/{accountId} | 
[**get_cloud_connected_sites**](ConfigurationMultiCloudApi.md#get_cloud_connected_sites) | **GET** /multicloud/connected-sites/{cloudType} | 
[**get_cloud_connected_sites1**](ConfigurationMultiCloudApi.md#get_cloud_connected_sites1) | **GET** /multicloud/connected-sites/edge/{edgeType} | 
[**get_cloud_devices**](ConfigurationMultiCloudApi.md#get_cloud_devices) | **GET** /multicloud/devices/{cloudType} | 
[**get_cloud_devices1**](ConfigurationMultiCloudApi.md#get_cloud_devices1) | **GET** /multicloud/devices/edge/{edgeType} | 
[**get_cloud_gateways**](ConfigurationMultiCloudApi.md#get_cloud_gateways) | **GET** /multicloud/cloudgateways/{cloudType} | 
[**get_cloud_regions**](ConfigurationMultiCloudApi.md#get_cloud_regions) | **GET** /multicloud/regions | 
[**get_cloud_routers_and_attachments**](ConfigurationMultiCloudApi.md#get_cloud_routers_and_attachments) | **GET** /multicloud/cloudRoutersAndAttachments | 
[**get_cloud_types**](ConfigurationMultiCloudApi.md#get_cloud_types) | **GET** /multicloud/types | 
[**get_cloud_widget**](ConfigurationMultiCloudApi.md#get_cloud_widget) | **GET** /multicloud/widget/{cloudType} | 
[**get_connectivity_gateway_creation_options**](ConfigurationMultiCloudApi.md#get_connectivity_gateway_creation_options) | **GET** /multicloud/connectivitygatewaycreationoptions | 
[**get_connectivity_gateways**](ConfigurationMultiCloudApi.md#get_connectivity_gateways) | **GET** /multicloud/connectivitygateway | 
[**get_dashboard_edge_info**](ConfigurationMultiCloudApi.md#get_dashboard_edge_info) | **GET** /multicloud/dashboard/edge | 
[**get_default_mapping_values**](ConfigurationMultiCloudApi.md#get_default_mapping_values) | **GET** /multicloud/map/defaults | 
[**get_device_link_metro_speed**](ConfigurationMultiCloudApi.md#get_device_link_metro_speed) | **POST** /multicloud/devicelink/metroSpeed/edge | 
[**get_device_links**](ConfigurationMultiCloudApi.md#get_device_links) | **GET** /multicloud/devicelink/edge | 
[**get_dl_port_speed**](ConfigurationMultiCloudApi.md#get_dl_port_speed) | **GET** /multicloud/devicelink/edge/portspeed/{edgeType} | 
[**get_edge_account_details**](ConfigurationMultiCloudApi.md#get_edge_account_details) | **GET** /multicloud/accounts/edge/{accountId} | 
[**get_edge_accounts**](ConfigurationMultiCloudApi.md#get_edge_accounts) | **GET** /multicloud/accounts/edge | 
[**get_edge_billing_accounts**](ConfigurationMultiCloudApi.md#get_edge_billing_accounts) | **GET** /multicloud/billingaccounts/edge/{edgeType}/{edgeAccountId} | 
[**get_edge_connectivity_detail_by_name**](ConfigurationMultiCloudApi.md#get_edge_connectivity_detail_by_name) | **GET** /multicloud/connectivity/edge/{connectivityName} | 
[**get_edge_connectivity_details**](ConfigurationMultiCloudApi.md#get_edge_connectivity_details) | **GET** /multicloud/connectivity/edge | 
[**get_edge_gateways**](ConfigurationMultiCloudApi.md#get_edge_gateways) | **GET** /multicloud/gateways/edge/{edgeType} | 
[**get_edge_global_settings**](ConfigurationMultiCloudApi.md#get_edge_global_settings) | **GET** /multicloud/settings/edge/global | 
[**get_edge_locations_info**](ConfigurationMultiCloudApi.md#get_edge_locations_info) | **GET** /multicloud/locations/edge/{edgeType} | 
[**get_edge_mapping_tags**](ConfigurationMultiCloudApi.md#get_edge_mapping_tags) | **GET** /multicloud/map/tags/edge | 
[**get_edge_types**](ConfigurationMultiCloudApi.md#get_edge_types) | **GET** /multicloud/types/edge | 
[**get_edge_wan_devices**](ConfigurationMultiCloudApi.md#get_edge_wan_devices) | **GET** /multicloud/edge/{edgeType}/device | 
[**get_edge_widget**](ConfigurationMultiCloudApi.md#get_edge_widget) | **GET** /multicloud/widget/edge/{edgeType} | 
[**get_global_settings**](ConfigurationMultiCloudApi.md#get_global_settings) | **GET** /multicloud/settings/global | 
[**get_host_vpcs**](ConfigurationMultiCloudApi.md#get_host_vpcs) | **GET** /multicloud/hostvpc | 
[**get_icgw_custom_setting_details**](ConfigurationMultiCloudApi.md#get_icgw_custom_setting_details) | **GET** /multicloud/gateway/edge/setting/{edgeGatewayName} | 
[**get_icgw_details**](ConfigurationMultiCloudApi.md#get_icgw_details) | **GET** /multicloud/gateway/edge/{edgeGatewayName} | 
[**get_icgw_types**](ConfigurationMultiCloudApi.md#get_icgw_types) | **GET** /multicloud/gateway/edge/types | 
[**get_icgws**](ConfigurationMultiCloudApi.md#get_icgws) | **GET** /multicloud/gateway/edge | 
[**get_licenses**](ConfigurationMultiCloudApi.md#get_licenses) | **GET** /multicloud/license/edge | 
[**get_mapping_matrix**](ConfigurationMultiCloudApi.md#get_mapping_matrix) | **GET** /multicloud/map | 
[**get_mapping_status**](ConfigurationMultiCloudApi.md#get_mapping_status) | **GET** /multicloud/map/status | 
[**get_mapping_summary**](ConfigurationMultiCloudApi.md#get_mapping_summary) | **GET** /multicloud/map/summary | 
[**get_mapping_tags**](ConfigurationMultiCloudApi.md#get_mapping_tags) | **GET** /multicloud/map/tags | 
[**get_mapping_vpns**](ConfigurationMultiCloudApi.md#get_mapping_vpns) | **GET** /multicloud/map/vpns | 
[**get_nva_security_rules**](ConfigurationMultiCloudApi.md#get_nva_security_rules) | **GET** /multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName} | 
[**get_partner_ports**](ConfigurationMultiCloudApi.md#get_partner_ports) | **GET** /multicloud/partnerports/edge | 
[**get_port_speed**](ConfigurationMultiCloudApi.md#get_port_speed) | **GET** /multicloud/portSpeed/edge/{edgeType}/{edgeAccountId}/{connectivityType} | 
[**get_post_aggregation_data_by_query25**](ConfigurationMultiCloudApi.md#get_post_aggregation_data_by_query25) | **POST** /multicloud/statistics/interface/aggregation | 
[**get_sites**](ConfigurationMultiCloudApi.md#get_sites) | **GET** /multicloud/site | 
[**get_sites1**](ConfigurationMultiCloudApi.md#get_sites1) | **GET** /multicloud/cloudgateway/{cloudGatewayName}/site | 
[**get_ssh_key_list**](ConfigurationMultiCloudApi.md#get_ssh_key_list) | **GET** /multicloud/sshkeys | 
[**get_supported_edge_image_names**](ConfigurationMultiCloudApi.md#get_supported_edge_image_names) | **GET** /multicloud/imagename/edge | 
[**get_supported_edge_instance_size**](ConfigurationMultiCloudApi.md#get_supported_edge_instance_size) | **GET** /multicloud/instancesize/edge | 
[**get_supported_instance_size**](ConfigurationMultiCloudApi.md#get_supported_instance_size) | **GET** /multicloud/instancesize | 
[**get_supported_loopback_cgw_colors**](ConfigurationMultiCloudApi.md#get_supported_loopback_cgw_colors) | **GET** /multicloud/loopbackCGWColor/edge | 
[**get_supported_loopback_transport_colors**](ConfigurationMultiCloudApi.md#get_supported_loopback_transport_colors) | **GET** /multicloud/loopbacktransportcolor/edge | 
[**get_supported_software_image_list**](ConfigurationMultiCloudApi.md#get_supported_software_image_list) | **GET** /multicloud/swimages | 
[**get_tunnel_names**](ConfigurationMultiCloudApi.md#get_tunnel_names) | **GET** /multicloud/tunnels/{cloudType} | 
[**get_v_hubs**](ConfigurationMultiCloudApi.md#get_v_hubs) | **GET** /multicloud/vhubs | 
[**get_v_wans**](ConfigurationMultiCloudApi.md#get_v_wans) | **GET** /multicloud/vwans | 
[**get_vpc_tags**](ConfigurationMultiCloudApi.md#get_vpc_tags) | **GET** /multicloud/hostvpc/tags | 
[**get_wan_devices**](ConfigurationMultiCloudApi.md#get_wan_devices) | **GET** /multicloud/device | 
[**get_wan_interface_colors**](ConfigurationMultiCloudApi.md#get_wan_interface_colors) | **GET** /multicloud/interfacecolor | 
[**hostvpc_tagging**](ConfigurationMultiCloudApi.md#hostvpc_tagging) | **POST** /multicloud/hostvpc/tags | 
[**process_mapping**](ConfigurationMultiCloudApi.md#process_mapping) | **POST** /multicloud/map | 
[**telemetry**](ConfigurationMultiCloudApi.md#telemetry) | **POST** /multicloud/telemetry | 
[**tunnel_scaling**](ConfigurationMultiCloudApi.md#tunnel_scaling) | **PUT** /multicloud/cloudgateway/{cloudGatewayName}/site | 
[**un_tag**](ConfigurationMultiCloudApi.md#un_tag) | **DELETE** /multicloud/hostvpc/tags/{tagName} | 
[**update_account**](ConfigurationMultiCloudApi.md#update_account) | **PUT** /multicloud/accounts/{accountId} | 
[**update_cgw**](ConfigurationMultiCloudApi.md#update_cgw) | **PUT** /multicloud/cloudgateway/{cloudGatewayName} | 
[**update_device_link**](ConfigurationMultiCloudApi.md#update_device_link) | **PUT** /multicloud/devicelink/edge | 
[**update_edge_account**](ConfigurationMultiCloudApi.md#update_edge_account) | **PUT** /multicloud/accounts/edge/{accountId} | 
[**update_edge_connectivity**](ConfigurationMultiCloudApi.md#update_edge_connectivity) | **PUT** /multicloud/connectivity/edge | 
[**update_edge_global_settings**](ConfigurationMultiCloudApi.md#update_edge_global_settings) | **PUT** /multicloud/settings/edge/global | 
[**update_edge_locations_info**](ConfigurationMultiCloudApi.md#update_edge_locations_info) | **PUT** /multicloud/locations/edge/{edgeType}/accountId/{accountId} | 
[**update_global_settings**](ConfigurationMultiCloudApi.md#update_global_settings) | **PUT** /multicloud/settings/global | 
[**update_icgw**](ConfigurationMultiCloudApi.md#update_icgw) | **PUT** /multicloud/gateway/edge/{edgeGatewayName} | 
[**update_nva_security_rules**](ConfigurationMultiCloudApi.md#update_nva_security_rules) | **PUT** /multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName} | 
[**validate_account_add**](ConfigurationMultiCloudApi.md#validate_account_add) | **POST** /multicloud/accounts | 
[**validate_account_update_credentials**](ConfigurationMultiCloudApi.md#validate_account_update_credentials) | **PUT** /multicloud/accounts/{accountId}/credentials | 
[**validate_edge_account_add**](ConfigurationMultiCloudApi.md#validate_edge_account_add) | **POST** /multicloud/accounts/edge | 
[**validate_edge_account_update_credentials**](ConfigurationMultiCloudApi.md#validate_edge_account_update_credentials) | **PUT** /multicloud/accounts/edge/{accountId}/credentials | 


# **add_edge_global_settings**
> add_edge_global_settings()



Add global settings for Edge provider

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_edge_global_settings(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->add_edge_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global setting | [optional]

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

# **add_global_settings**
> add_global_settings()



Acquire ip from resource pool

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_global_settings(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->add_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global setting | [optional]

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

# **attach_sites**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} attach_sites(cloud_gateway_name)



Attach sites to cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Site information (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attach_sites(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->attach_sites: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attach_sites(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->attach_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Site information | [optional]

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

# **audit**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} audit()



Call an audit

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Audit (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.audit(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Audit | [optional]

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

# **audit_dry_run**
> audit_dry_run()



Call an audit with dry run

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)
    cloud_region = "cloudRegion_example" # str | Region (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.audit_dry_run(cloud_type=cloud_type, cloud_region=cloud_region)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->audit_dry_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]
 **cloud_region** | **str**| Region | [optional]

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

# **clean_up_all_connectivity_gateways_in_local_db**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} clean_up_all_connectivity_gateways_in_local_db()



Delete all Connectivity Gateways in local DB

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    deletion_type = "deletionType_example" # str | Deletion Type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.clean_up_all_connectivity_gateways_in_local_db(deletion_type=deletion_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->clean_up_all_connectivity_gateways_in_local_db: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deletion_type** | **str**| Deletion Type | [optional]

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

# **create_cgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cgw()



Create cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloud gateway (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cgw(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_cgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloud gateway | [optional]

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

# **create_connectivity_gateway**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connectivity_gateway()



Create Connectivity gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Connectivity gateway (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_connectivity_gateway(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_connectivity_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Connectivity gateway | [optional]

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

# **create_device_link**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_device_link()



Create Device Link

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device Link (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_device_link(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_device_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device Link | [optional]

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

# **create_edge_connectivity**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_edge_connectivity()



Create Interconnect connectivity

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Edge connectivity (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_edge_connectivity(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_edge_connectivity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Edge connectivity | [optional]

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

# **create_icgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_icgw()



Create Interconnect Gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Interconnect Gateway (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_icgw(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_icgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Interconnect Gateway | [optional]

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

# **create_virtual_wan**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_virtual_wan()



Create Virtual WAN

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Virtual WAN (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_virtual_wan(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->create_virtual_wan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Virtual WAN | [optional]

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

# **delete_account**
> delete_account(account_id)



Delete cloud account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_account(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |

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

# **delete_cgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_cgw(cloud_gateway_name)



Delete cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    delete_all_resources = True # bool | Optional Flag for deletion of Azure Resource Group, Default: True (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_cgw(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_cgw: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_cgw(cloud_gateway_name, delete_all_resources=delete_all_resources)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_cgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **delete_all_resources** | **bool**| Optional Flag for deletion of Azure Resource Group, Default: True | [optional]

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

# **delete_connectivity_gateway**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_connectivity_gateway(cloud_provider, connectivity_gateway_name)



Delete Connectivity Gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_provider = "cloudProvider_example" # str | Cloud Provider
    connectivity_gateway_name = "connectivityGatewayName_example" # str | Connectivity gateway name
    connectivity_type = "connectivityType_example" # str | Cloud Connectivity Type (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_connectivity_gateway(cloud_provider, connectivity_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_connectivity_gateway: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_connectivity_gateway(cloud_provider, connectivity_gateway_name, connectivity_type=connectivity_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_connectivity_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| Cloud Provider |
 **connectivity_gateway_name** | **str**| Connectivity gateway name |
 **connectivity_type** | **str**| Cloud Connectivity Type | [optional]

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

# **delete_device_link**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_device_link(device_link_name)



Delete Device Link

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    device_link_name = "deviceLinkName_example" # str | Device Link Name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_device_link(device_link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_device_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_link_name** | **str**| Device Link Name |

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

# **delete_edge_account**
> delete_edge_account(account_id)



Delete edge account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Edge Account Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_edge_account(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_edge_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Edge Account Id |

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

# **delete_edge_account1**
> delete_edge_account1()



Delete edge account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_edge_account1()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_edge_account1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge Type | defaults to "MEGAPORT"

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

# **delete_edge_connectivity**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_edge_connectivity(connection_name)



Delete Interconnect connectivity

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    connection_name = "connectionName_example" # str | Edge connectivity name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_edge_connectivity(connection_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_edge_connectivity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Edge connectivity name |

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

# **delete_icgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_icgw(edge_gateway_name)



Delete Interconnect Gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_gateway_name = "edgeGatewayName_example" # str | Edge gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_icgw(edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_icgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_gateway_name** | **str**| Edge gateway name |

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

# **delete_virtual_wan**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_virtual_wan(cloud_provider, v_wan_name)



Delete Virtual Wan

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_provider = "cloudProvider_example" # str | Cloud Provider
    v_wan_name = "vWanName_example" # str | Virtual Wan name
    account_id = "accountId_example" # str | Account Id (optional)
    resource_group = "resourceGroup_example" # str | Resource Group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_virtual_wan(cloud_provider, v_wan_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_virtual_wan: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_virtual_wan(cloud_provider, v_wan_name, account_id=account_id, resource_group=resource_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->delete_virtual_wan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| Cloud Provider |
 **v_wan_name** | **str**| Virtual Wan name |
 **account_id** | **str**| Account Id | [optional]
 **resource_group** | **str**| Resource Group | [optional]

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

# **detach_sites1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} detach_sites1(cloud_gateway_name)



Detach sites from cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Site information (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.detach_sites1(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->detach_sites1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.detach_sites1(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->detach_sites1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Site information | [optional]

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

# **edge_audit**
> edge_audit()



Call an edge audit

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type (optional)
    cloud_type = "cloudType_example" # str | Cloud type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edge_audit(edge_type=edge_type, cloud_type=cloud_type)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->edge_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **cloud_type** | **str**| Cloud type | [optional]

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

# **edge_audit_dry_run**
> edge_audit_dry_run()



Call an edge audit with dry run

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type (optional)
    cloud_type = "cloudType_example" # str | Cloud type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edge_audit_dry_run(edge_type=edge_type, cloud_type=cloud_type)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->edge_audit_dry_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **cloud_type** | **str**| Cloud type | [optional]

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

# **edit_tag**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_tag()



Edit VPCs for a tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC tag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_tag(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->edit_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC tag | [optional]

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

# **get_all_cloud_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_cloud_accounts()



Get All cloud accounts

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)
    cloud_gateway_enabled = True # bool | Cloud gateway enabled flag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_cloud_accounts(cloud_type=cloud_type, cloud_gateway_enabled=cloud_gateway_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_all_cloud_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]
 **cloud_gateway_enabled** | **bool**| Cloud gateway enabled flag | [optional]

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

# **get_azure_network_virtual_appliances**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_network_virtual_appliances(cloud_type, accound_id, region, resource_group_name, resource_group_source, vhub_name, vhub_source)



Discover Azure Virtual NVAs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AZURE" # str | Cloud type
    accound_id = "accoundId_example" # str | Account ID
    region = "region_example" # str | Region
    resource_group_name = "resourceGroupName_example" # str | Resource Group Name
    resource_group_source = "resourceGroupSource_example" # str | Resource Group Source
    vhub_name = "vhubName_example" # str | VHUB name
    vhub_source = "vhubSource_example" # str | VHUB source

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_azure_network_virtual_appliances(cloud_type, accound_id, region, resource_group_name, resource_group_source, vhub_name, vhub_source)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_azure_network_virtual_appliances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **accound_id** | **str**| Account ID |
 **region** | **str**| Region |
 **resource_group_name** | **str**| Resource Group Name |
 **resource_group_source** | **str**| Resource Group Source |
 **vhub_name** | **str**| VHUB name |
 **vhub_source** | **str**| VHUB source |

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

# **get_azure_nva_sku_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_nva_sku_list(cloud_type)



Get Azure NVA SKUs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_azure_nva_sku_list(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_azure_nva_sku_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**|  |

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

# **get_azure_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_resource_groups(cloud_type, account_id)



Discover Azure Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AZURE" # str | Cloud type
    account_id = "accountId_example" # str | Account ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_azure_resource_groups(cloud_type, account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_azure_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **account_id** | **str**| Account ID |

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

# **get_azure_virtual_hubs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_virtual_hubs(cloud_type, accound_id, region, resource_group_name, resource_group_source, vwan_name, vwan_source)



Discover Azure Virtual HUBs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AZURE" # str | Cloud type
    accound_id = "accoundId_example" # str | Account ID
    region = "region_example" # str | Region
    resource_group_name = "resourceGroupName_example" # str | Resource Group Name
    resource_group_source = "resourceGroupSource_example" # str | Resource Group Source
    vwan_name = "vwanName_example" # str | VWAN name
    vwan_source = "vwanSource_example" # str | VWAN source

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_azure_virtual_hubs(cloud_type, accound_id, region, resource_group_name, resource_group_source, vwan_name, vwan_source)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_azure_virtual_hubs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **accound_id** | **str**| Account ID |
 **region** | **str**| Region |
 **resource_group_name** | **str**| Resource Group Name |
 **resource_group_source** | **str**| Resource Group Source |
 **vwan_name** | **str**| VWAN name |
 **vwan_source** | **str**| VWAN source |

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

# **get_azure_virtual_wans**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_virtual_wans(cloud_type, accound_id, resource_group_name, resource_group_source)



Discover Azure Virtual WANs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AZURE" # str | Cloud type
    accound_id = "accoundId_example" # str | Account ID
    resource_group_name = "resourceGroupName_example" # str | Resource Group Name
    resource_group_source = "resourceGroupSource_example" # str | Resource Group Source

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_azure_virtual_wans(cloud_type, accound_id, resource_group_name, resource_group_source)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_azure_virtual_wans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **accound_id** | **str**| Account ID |
 **resource_group_name** | **str**| Resource Group Name |
 **resource_group_source** | **str**| Resource Group Source |

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

# **get_cgw_associated_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgw_associated_mappings(cloud_type, cloud_gateway_name)



Get associated mappings to the CGW

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud Gateway Name
    site_uuid = "siteUuid_example" # str | Site Device UUID (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cgw_associated_mappings(cloud_type, cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_associated_mappings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cgw_associated_mappings(cloud_type, cloud_gateway_name, site_uuid=site_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_associated_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **cloud_gateway_name** | **str**| Cloud Gateway Name |
 **site_uuid** | **str**| Site Device UUID | [optional]

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

# **get_cgw_custom_setting_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgw_custom_setting_details(cloud_gateway_name)



Get cloud gateway custom setting by cloud gateway name

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cgw_custom_setting_details(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_custom_setting_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |

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

# **get_cgw_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgw_details(cloud_gateway_name)



Get cloud gateway by name

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cgw_details(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |

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

# **get_cgw_org_resources**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgw_org_resources(cloud_gateway_name)



Get cloud gateways

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cgw_org_resources(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_org_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |

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

# **get_cgw_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgw_types()



Get cloud gateway types for specified cloudType

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cgw_types(cloud_type=cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgw_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]

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

# **get_cgws**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cgws()



Get cloud gateways

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)
    account_id = "accountId_example" # str | Account Id (optional)
    region = "region_example" # str | Region (optional)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name (optional)
    connectivity_state = "connectivityState_example" # str | Connectivity State (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cgws(cloud_type=cloud_type, account_id=account_id, region=region, cloud_gateway_name=cloud_gateway_name, connectivity_state=connectivity_state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cgws: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]
 **account_id** | **str**| Account Id | [optional]
 **region** | **str**| Region | [optional]
 **cloud_gateway_name** | **str**| Cloud gateway name | [optional]
 **connectivity_state** | **str**| Connectivity State | [optional]

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

# **get_cloud_account_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_account_details(account_id)



Get cloud account by account Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_account_details(account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_account_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |

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

# **get_cloud_connected_sites**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_connected_sites(cloud_type)



Get sites with connectivity to the cloud by cloud type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud Gateway Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_connected_sites(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_connected_sites: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_connected_sites(cloud_type, cloud_gateway_name=cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_connected_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **cloud_gateway_name** | **str**| Cloud Gateway Name | [optional]

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

# **get_cloud_connected_sites1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_connected_sites1(edge_type)



Get sites with connectivity to the interconnect gateways by edge type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type
    edge_gateway_name = "edgeGatewayName_example" # str | Interconnect Gateway Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_connected_sites1(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_connected_sites1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_connected_sites1(edge_type, edge_gateway_name=edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_connected_sites1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type |
 **edge_gateway_name** | **str**| Interconnect Gateway Name | [optional]

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

# **get_cloud_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_devices(cloud_type)



Get cloud devices by cloud type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud Gateway Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_devices(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_devices(cloud_type, cloud_gateway_name=cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **cloud_gateway_name** | **str**| Cloud Gateway Name | [optional]

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

# **get_cloud_devices1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_devices1(edge_type)



Get cloud devices by cloud type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type
    edge_gateway_name = "edgeGatewayName_example" # str | Edge Gateway Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_devices1(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_devices1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_devices1(edge_type, edge_gateway_name=edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_devices1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type |
 **edge_gateway_name** | **str**| Edge Gateway Name | [optional]

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

# **get_cloud_gateways**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_gateways(cloud_type)



Get sites with connectivity to the cloud by cloud type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_gateways(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_gateways: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_cloud_regions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_regions()



Get cloud regions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_regions(cloud_type=cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]

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

# **get_cloud_routers_and_attachments**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_routers_and_attachments()



Get all Cloud Routers and their Attachments

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id (optional)
    region = "region_example" # str | Region (optional)
    network = "network_example" # str | Network (optional)
    connectivity_gateway_name = "connectivityGatewayName_example" # str | Connectivity Gateway Name (optional)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud Gateway Name (optional)
    state = "state_example" # str | State (optional)
    refresh = "refresh_example" # str | Refresh (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_routers_and_attachments(account_id=account_id, region=region, network=network, connectivity_gateway_name=connectivity_gateway_name, cloud_gateway_name=cloud_gateway_name, state=state, refresh=refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_routers_and_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | [optional]
 **region** | **str**| Region | [optional]
 **network** | **str**| Network | [optional]
 **connectivity_gateway_name** | **str**| Connectivity Gateway Name | [optional]
 **cloud_gateway_name** | **str**| Cloud Gateway Name | [optional]
 **state** | **str**| State | [optional]
 **refresh** | **str**| Refresh | [optional]

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

# **get_cloud_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_types()



Get cloud types

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_types()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_types: %s\n" % e)
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

# **get_cloud_widget**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_widget(cloud_type)



Get cloud widget by cloud type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_widget(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_cloud_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_connectivity_gateway_creation_options**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_connectivity_gateway_creation_options()



Get connectivity gateway creation options

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id (optional)
    cloud_type = "cloudType_example" # str | Cloud Type (optional)
    connectivity_type = "connectivityType_example" # str | Cloud Connectivity Type (optional)
    refresh = "refresh_example" # str | Refresh (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_connectivity_gateway_creation_options(account_id=account_id, cloud_type=cloud_type, connectivity_type=connectivity_type, refresh=refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_connectivity_gateway_creation_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | [optional]
 **cloud_type** | **str**| Cloud Type | [optional]
 **connectivity_type** | **str**| Cloud Connectivity Type | [optional]
 **refresh** | **str**| Refresh | [optional]

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

# **get_connectivity_gateways**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_connectivity_gateways()



Get all Connectivity Gateways

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id (optional)
    cloud_type = "cloudType_example" # str | Cloud Type (optional)
    connectivity_type = "connectivityType_example" # str | Cloud Connectivity Type (optional)
    connectivity_gateway_name = "connectivityGatewayName_example" # str | Connectivity Gateway Name (optional)
    region = "region_example" # str | Region (optional)
    network = "network_example" # str | Network (optional)
    state = "state_example" # str | State (optional)
    refresh = "refresh_example" # str | Refresh (optional)
    edge_type = "MEGAPORT" # str | Edge type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_connectivity_gateways(account_id=account_id, cloud_type=cloud_type, connectivity_type=connectivity_type, connectivity_gateway_name=connectivity_gateway_name, region=region, network=network, state=state, refresh=refresh, edge_type=edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_connectivity_gateways: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | [optional]
 **cloud_type** | **str**| Cloud Type | [optional]
 **connectivity_type** | **str**| Cloud Connectivity Type | [optional]
 **connectivity_gateway_name** | **str**| Connectivity Gateway Name | [optional]
 **region** | **str**| Region | [optional]
 **network** | **str**| Network | [optional]
 **state** | **str**| State | [optional]
 **refresh** | **str**| Refresh | [optional]
 **edge_type** | **str**| Edge type | [optional]

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

# **get_dashboard_edge_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dashboard_edge_info()



Get interconnect edge gateway dashboard info

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dashboard_edge_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_dashboard_edge_info: %s\n" % e)
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

# **get_default_mapping_values**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_default_mapping_values(cloud_type)



Get default mapping values

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_default_mapping_values(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_default_mapping_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_device_link_metro_speed**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_link_metro_speed()



Get Device Link Metro Speed based on device link config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device Link (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_link_metro_speed(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_device_link_metro_speed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device Link | [optional]

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

# **get_device_links**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_links()



Get Device Links

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional)
    device_link_name = "deviceLinkName_example" # str | Device Link Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_links(edge_type=edge_type, device_link_name=device_link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_device_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **device_link_name** | **str**| Device Link Name | [optional]

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

# **get_dl_port_speed**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dl_port_speed(edge_type)



Get supported port speed for Device Link

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Interconnect Provider

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dl_port_speed(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_dl_port_speed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Interconnect Provider |

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

# **get_edge_account_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_account_details(account_id)



Get edge account by account Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Edge Account Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_account_details(account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_account_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Edge Account Id |

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

# **get_edge_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_accounts()



Get all Multicloud edge accounts

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional) if omitted the server will use the default value of "MEGAPORT"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_edge_accounts(edge_type=edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional] if omitted the server will use the default value of "MEGAPORT"

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

# **get_edge_billing_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_billing_accounts(edge_account_id)



Get Edge Billing Accounts

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_account_id = "edgeAccountId_example" # str | Interconnect Provider Account ID
    region = "region_example" # str | Region (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_billing_accounts(edge_account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_billing_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_edge_billing_accounts(edge_account_id, region=region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_billing_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_account_id** | **str**| Interconnect Provider Account ID |
 **edge_type** | **str**| Interconnect Provider | defaults to "EQUINIX"
 **region** | **str**| Region | [optional]

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

# **get_edge_connectivity_detail_by_name**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_connectivity_detail_by_name(connectivity_name)



Get Interconnect Connectivity by name

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    connectivity_name = "connectivityName_example" # str | IC-GW connectivity name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_connectivity_detail_by_name(connectivity_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_connectivity_detail_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_name** | **str**| IC-GW connectivity name |

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

# **get_edge_connectivity_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_connectivity_details()



Get Interconnect Connectivity details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional)
    connectivity_name = "connectivityName_example" # str | Connectivity Name (optional)
    connectivity_type = "connectivityType_example" # str | Connectivity Type (optional)
    edge_gateway_name = "edgeGatewayName_example" # str | Interconnect Gateway name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_edge_connectivity_details(edge_type=edge_type, connectivity_name=connectivity_name, connectivity_type=connectivity_type, edge_gateway_name=edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_connectivity_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **connectivity_name** | **str**| Connectivity Name | [optional]
 **connectivity_type** | **str**| Connectivity Type | [optional]
 **edge_gateway_name** | **str**| Interconnect Gateway name | [optional]

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

# **get_edge_gateways**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_gateways(edge_type)



Get sites with connectivity to the interconnect gateways by edge type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_gateways(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_gateways: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type |

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

# **get_edge_global_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_global_settings(edge_type)



Get edge global settings

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MP" # str | Edge type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_global_settings(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type |

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

# **get_edge_locations_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_locations_info()



Get Edge Locations

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Edge Account Id (optional)
    region = "region_example" # str | Region (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_locations_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_locations_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_edge_locations_info(account_id=account_id, region=region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_locations_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge Type | defaults to "MEGAPORT"
 **account_id** | **str**| Edge Account Id | [optional]
 **region** | **str**| Region | [optional]

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

# **get_edge_mapping_tags**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_mapping_tags(cloud_type)



Get default Interconnect mapping tag values

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type
    account_id = "accountId_example" # str | Cloud Account Id (optional)
    resource_group = "resourceGroup_example" # str | Resource Group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_mapping_tags(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_mapping_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_edge_mapping_tags(cloud_type, account_id=account_id, resource_group=resource_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_mapping_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **account_id** | **str**| Cloud Account Id | [optional]
 **resource_group** | **str**| Resource Group | [optional]

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

# **get_edge_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_types()



Get edge types

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_edge_types()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_types: %s\n" % e)
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

# **get_edge_wan_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_wan_devices()



Get available WAN edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_wan_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_wan_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge Type | defaults to "MEGAPORT"

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

# **get_edge_widget**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_edge_widget(edge_type)



Get Interconnect Edge widget by edge type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "edgeType_example" # str | Edge type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_edge_widget(edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_edge_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type |

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

# **get_global_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_global_settings(cloud_type)



Get global settings

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_global_settings(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_host_vpcs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_host_vpcs(cloud_type)



Get tagged, untagged, or all Host VPCs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type
    account_ids = "accountIds_example" # str | Account Id (optional)
    region = "region_example" # str | Region (optional)
    untagged = "untagged_example" # str | Untagged flag (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_host_vpcs(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_host_vpcs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_host_vpcs(cloud_type, account_ids=account_ids, region=region, untagged=untagged)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_host_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **account_ids** | **str**| Account Id | [optional]
 **region** | **str**| Region | [optional]
 **untagged** | **str**| Untagged flag | [optional]

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

# **get_icgw_custom_setting_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_icgw_custom_setting_details(edge_gateway_name)



Get Interconnect Gateway custom setting by Interconnect Gateway name

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_gateway_name = "edgeGatewayName_example" # str | Edge gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_icgw_custom_setting_details(edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_icgw_custom_setting_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_gateway_name** | **str**| Edge gateway name |

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

# **get_icgw_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_icgw_details(edge_gateway_name)



Get Interconnect Gateway by name

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_gateway_name = "edgeGatewayName_example" # str | Edge gateway name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_icgw_details(edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_icgw_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_gateway_name** | **str**| Edge gateway name |

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

# **get_icgw_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_icgw_types()



Get Interconnect Gateway type for specified Edge Provider

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_icgw_types(edge_type=edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_icgw_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]

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

# **get_icgws**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_icgws()



Get Interconnect Gateways

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional)
    account_id = "accountId_example" # str | Account Id (optional)
    region = "region_example" # str | Region (optional)
    region_id = "regionId_example" # str | Region Id (optional)
    resource_state = "resourceState_example" # str | Resource State (optional)
    edge_gateway_name = "edgeGatewayName_example" # str | Edge gateway name (optional)
    billing_account_id = "billingAccountId_example" # str | billing Account Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_icgws(edge_type=edge_type, account_id=account_id, region=region, region_id=region_id, resource_state=resource_state, edge_gateway_name=edge_gateway_name, billing_account_id=billing_account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_icgws: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **account_id** | **str**| Account Id | [optional]
 **region** | **str**| Region | [optional]
 **region_id** | **str**| Region Id | [optional]
 **resource_state** | **str**| Resource State | [optional]
 **edge_gateway_name** | **str**| Edge gateway name | [optional]
 **billing_account_id** | **str**| billing Account Id | [optional]

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

# **get_licenses**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_licenses()



Get License Info for Edge Gateways/Connections

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional) if omitted the server will use the default value of "MEGAPORT"
    account_id = "accountId_example" # str | Edge Account Id (optional)
    product_type = "GATEWAY" # str | product Type (optional)
    refresh = "refresh_example" # str | Refresh License Cache from Megaport (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_licenses(edge_type=edge_type, account_id=account_id, product_type=product_type, refresh=refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_licenses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional] if omitted the server will use the default value of "MEGAPORT"
 **account_id** | **str**| Edge Account Id | [optional]
 **product_type** | **str**| product Type | [optional]
 **refresh** | **str**| Refresh License Cache from Megaport | [optional]

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

# **get_mapping_matrix**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapping_matrix(cloud_type)



Get default mapping values

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mapping_matrix(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_mapping_matrix: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_mapping_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapping_status()



Get mapping status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type (optional)
    region = "region_example" # str | Region (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_mapping_status(cloud_type=cloud_type, region=region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_mapping_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type | [optional]
 **region** | **str**| Region | [optional]

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

# **get_mapping_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapping_summary()



Get mapping summary

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    vpn_tunnel_status = True # bool | VPN tunnel status (optional)
    cloud_type = "AWS" # str | Cloud type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_mapping_summary(vpn_tunnel_status=vpn_tunnel_status, cloud_type=cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_mapping_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_tunnel_status** | **bool**| VPN tunnel status | [optional]
 **cloud_type** | **str**| Cloud type | [optional]

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

# **get_mapping_tags**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapping_tags(cloud_type)



Get default mapping values

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mapping_tags(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_mapping_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |

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

# **get_mapping_vpns**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapping_vpns()



Get default mapping values

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_mapping_vpns()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_mapping_vpns: %s\n" % e)
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

# **get_nva_security_rules**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_nva_security_rules(cloud_gateway_name)



Get NVA Security Rules

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Get NVA security Rules (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_nva_security_rules(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_nva_security_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_nva_security_rules(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_nva_security_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Get NVA security Rules | [optional]

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

# **get_partner_ports**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_partner_ports()



Get partner ports

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional)
    account_id = "accountId_example" # str | Edge Account Id (optional)
    cloud_type = "cloudType_example" # str | Cloud Type (optional)
    connect_type = "connectType_example" # str | Connect Type filter (optional)
    vxc_permitted = "vxcPermitted_example" # str | VXC Permitted on the port (optional)
    authorization_key = "authorizationKey_example" # str | authorization Key (optional)
    refresh = "refresh_example" # str | Refresh (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_partner_ports(edge_type=edge_type, account_id=account_id, cloud_type=cloud_type, connect_type=connect_type, vxc_permitted=vxc_permitted, authorization_key=authorization_key, refresh=refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_partner_ports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional]
 **account_id** | **str**| Edge Account Id | [optional]
 **cloud_type** | **str**| Cloud Type | [optional]
 **connect_type** | **str**| Connect Type filter | [optional]
 **vxc_permitted** | **str**| VXC Permitted on the port | [optional]
 **authorization_key** | **str**| authorization Key | [optional]
 **refresh** | **str**| Refresh | [optional]

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

# **get_port_speed**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_port_speed(edge_type, edge_account_id, connectivity_type)



Get supported port speed

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Interconnect Provider
    edge_account_id = "edgeAccountId_example" # str | Interconnect Provider Account ID
    connectivity_type = "connectivityType_example" # str | Interconnect Connectivity Type
    cloud_type = "AWS" # str | Cloud Service Provider (optional)
    cloud_account_id = "cloudAccountId_example" # str | Cloud Service Provider Account ID (optional)
    connect_type = "connectType_example" # str | Connection Type filter (optional)
    connect_sub_type = "connectSubType_example" # str | Connection Sub-Type filter (optional)
    connectivity_gateway = "connectivityGateway_example" # str | Connectivity Gateway (optional)
    partner_port = "partnerPort_example" # str | partnerPort (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_port_speed(edge_type, edge_account_id, connectivity_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_port_speed: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_port_speed(edge_type, edge_account_id, connectivity_type, cloud_type=cloud_type, cloud_account_id=cloud_account_id, connect_type=connect_type, connect_sub_type=connect_sub_type, connectivity_gateway=connectivity_gateway, partner_port=partner_port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_port_speed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Interconnect Provider |
 **edge_account_id** | **str**| Interconnect Provider Account ID |
 **connectivity_type** | **str**| Interconnect Connectivity Type |
 **cloud_type** | **str**| Cloud Service Provider | [optional]
 **cloud_account_id** | **str**| Cloud Service Provider Account ID | [optional]
 **connect_type** | **str**| Connection Type filter | [optional]
 **connect_sub_type** | **str**| Connection Sub-Type filter | [optional]
 **connectivity_gateway** | **str**| Connectivity Gateway | [optional]
 **partner_port** | **str**| partnerPort | [optional]

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

# **get_post_aggregation_data_by_query25**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query25()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query25(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_post_aggregation_data_by_query25: %s\n" % e)
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

# **get_sites**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sites()



Get available sites

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    color = "color_example" # str | Color (optional)
    attached = True # bool | Is endpoint attached (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sites(color=color, attached=attached)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **str**| Color | [optional]
 **attached** | **bool**| Is endpoint attached | [optional]

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

# **get_sites1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sites1(cloud_gateway_name)



Get sites attached to CGW

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    system_ip = "systemIp_example" # str | System IP (optional)
    site_id = "siteId_example" # str | Site Id (optional)
    color = "color_example" # str | Color (optional)
    vpn_tunnel_status = True # bool | Fetch vpnTunnelStatus (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sites1(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_sites1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sites1(cloud_gateway_name, system_ip=system_ip, site_id=site_id, color=color, vpn_tunnel_status=vpn_tunnel_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_sites1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **system_ip** | **str**| System IP | [optional]
 **site_id** | **str**| Site Id | [optional]
 **color** | **str**| Color | [optional]
 **vpn_tunnel_status** | **bool**| Fetch vpnTunnelStatus | [optional]

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

# **get_ssh_key_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ssh_key_list(cloud_type, account_id, cloud_region)



Get SSH keys

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type
    account_id = "accountId_example" # str | Account Id
    cloud_region = "cloudRegion_example" # str | Region

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ssh_key_list(cloud_type, account_id, cloud_region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_ssh_key_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **account_id** | **str**| Account Id |
 **cloud_region** | **str**| Region |

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

# **get_supported_edge_image_names**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_edge_image_names()



Get Edge provider supported images

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional) if omitted the server will use the default value of "MEGAPORT"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_supported_edge_image_names(edge_type=edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_edge_image_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional] if omitted the server will use the default value of "MEGAPORT"

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

# **get_supported_edge_instance_size**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_edge_instance_size()



Get Edge provider supported size

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_type = "MEGAPORT" # str | Edge type (optional) if omitted the server will use the default value of "MEGAPORT"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_supported_edge_instance_size(edge_type=edge_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_edge_instance_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| Edge type | [optional] if omitted the server will use the default value of "MEGAPORT"

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

# **get_supported_instance_size**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_instance_size(cloud_type)



Get Transit VPC supported size

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | 
    account_id = "accountId_example" # str |  (optional)
    cloud_region = "cloudRegion_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_supported_instance_size(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_instance_size: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_supported_instance_size(cloud_type, account_id=account_id, cloud_region=cloud_region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_instance_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**|  |
 **account_id** | **str**|  | [optional]
 **cloud_region** | **str**|  | [optional]

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

# **get_supported_loopback_cgw_colors**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_loopback_cgw_colors()



Get Edge Loopback CGW supported colors

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_supported_loopback_cgw_colors()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_loopback_cgw_colors: %s\n" % e)
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

# **get_supported_loopback_transport_colors**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_loopback_transport_colors()



Get Edge Loopback Tunnel supported colors

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_supported_loopback_transport_colors()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_loopback_transport_colors: %s\n" % e)
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

# **get_supported_software_image_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_supported_software_image_list(cloud_type)



Get software image list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type
    account_id = "accountId_example" # str | Account Id (optional)
    cloud_region = "cloudRegion_example" # str | Region (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_supported_software_image_list(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_software_image_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_supported_software_image_list(cloud_type, account_id=account_id, cloud_region=cloud_region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_supported_software_image_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **account_id** | **str**| Account Id | [optional]
 **cloud_region** | **str**| Region | [optional]

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

# **get_tunnel_names**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnel_names(cloud_type)



Get tunnel names

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud type
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tunnel_names(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_tunnel_names: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tunnel_names(cloud_type, cloud_gateway_name=cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_tunnel_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **cloud_gateway_name** | **str**| Cloud gateway name | [optional]

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

# **get_v_hubs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_hubs()



Get Virtual Hubs

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "cloudType_example" # str | Cloud Type (optional)
    account_id = "accountId_example" # str | Account Id (optional)
    resource_group = "resourceGroup_example" # str | Resource Group (optional)
    v_wan_name = "vWanName_example" # str | VWan Name (optional)
    v_net_tags = "vNetTags_example" # str | VNet Tags (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_v_hubs(cloud_type=cloud_type, account_id=account_id, resource_group=resource_group, v_wan_name=v_wan_name, v_net_tags=v_net_tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_v_hubs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud Type | [optional]
 **account_id** | **str**| Account Id | [optional]
 **resource_group** | **str**| Resource Group | [optional]
 **v_wan_name** | **str**| VWan Name | [optional]
 **v_net_tags** | **str**| VNet Tags | [optional]

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

# **get_v_wans**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_wans()



Get Virtual Wans

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id (optional)
    cloud_type = "cloudType_example" # str | Cloud Type (optional)
    resource_group = "resourceGroup_example" # str | Resource Group (optional)
    refresh = "refresh_example" # str | Refresh (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_v_wans(account_id=account_id, cloud_type=cloud_type, resource_group=resource_group, refresh=refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_v_wans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | [optional]
 **cloud_type** | **str**| Cloud Type | [optional]
 **resource_group** | **str**| Resource Group | [optional]
 **refresh** | **str**| Refresh | [optional]

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

# **get_vpc_tags**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vpc_tags(cloud_type)



Get vpc tags

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_type = "AWS" # str | Cloud type
    region = "region_example" # str | Region (optional)
    tag_name = "tagName_example" # str | Tag name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vpc_tags(cloud_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_vpc_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vpc_tags(cloud_type, region=region, tag_name=tag_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_vpc_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_type** | **str**| Cloud type |
 **region** | **str**| Region | [optional]
 **tag_name** | **str**| Tag name | [optional]

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

# **get_wan_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_wan_devices()



Get available WAN edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_wan_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_wan_devices: %s\n" % e)
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

# **get_wan_interface_colors**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_wan_interface_colors()



Get WAN interface colors

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_wan_interface_colors()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->get_wan_interface_colors: %s\n" % e)
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

# **hostvpc_tagging**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} hostvpc_tagging()



Tag a VPC

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC tag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.hostvpc_tagging(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->hostvpc_tagging: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC tag | [optional]

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

# **process_mapping**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_mapping()



Process intent of connecting VPNs with VPCs through cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC mapping (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_mapping(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->process_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC mapping | [optional]

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

# **telemetry**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} telemetry()



reports telemetry data

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | telemetry (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.telemetry(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->telemetry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| telemetry | [optional]

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

# **tunnel_scaling**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} tunnel_scaling(cloud_gateway_name)



Update tunnel scaling and accelerated vpn parameter for a branch endpoint

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Site information (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tunnel_scaling(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->tunnel_scaling: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tunnel_scaling(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->tunnel_scaling: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Site information | [optional]

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

# **un_tag**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} un_tag(tag_name)



Delete a tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    tag_name = "tagName_example" # str | Tag name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.un_tag(tag_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->un_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name |

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

# **update_account**
> update_account(account_id)



Update multicloud account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud account info (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_account(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_account(account_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud account info | [optional]

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

# **update_cgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_cgw(cloud_gateway_name)



Update cloud gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloud gateway (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_cgw(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_cgw: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_cgw(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_cgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloud gateway | [optional]

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

# **update_device_link**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_device_link()



Update Device Link

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device Link (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_device_link(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_device_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device Link | [optional]

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

# **update_edge_account**
> update_edge_account(account_id)



Update Multicloud edge account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Multicloud Edge Account Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud edge account info (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_edge_account(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_edge_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_edge_account(account_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_edge_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Multicloud Edge Account Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud edge account info | [optional]

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

# **update_edge_connectivity**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_edge_connectivity()



Update Interconnect connectivity

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Edge connectivity (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_edge_connectivity(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_edge_connectivity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Edge connectivity | [optional]

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

# **update_edge_global_settings**
> update_edge_global_settings()



Update edge global settings for Edge provider

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_edge_global_settings(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_edge_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global setting | [optional]

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

# **update_edge_locations_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_edge_locations_info(account_id)



Update Edge Locations

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Edge Account Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_edge_locations_info(account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_edge_locations_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Edge Account Id |
 **edge_type** | **str**| Edge Type | defaults to "MEGAPORT"

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

# **update_global_settings**
> update_global_settings()



Update ip in resource pool

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_global_settings(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_global_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global setting | [optional]

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

# **update_icgw**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_icgw(edge_gateway_name)



Update Interconnect Gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    edge_gateway_name = "edgeGatewayName_example" # str | Edge gateway name
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_icgw(edge_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_icgw: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_icgw(edge_gateway_name, get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_icgw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_gateway_name** | **str**| Edge gateway name |
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **update_nva_security_rules**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_nva_security_rules(cloud_gateway_name)



Update NVA Security Rules

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    cloud_gateway_name = "cloudGatewayName_example" # str | Cloud gateway name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update NVA security Rules (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_nva_security_rules(cloud_gateway_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_nva_security_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_nva_security_rules(cloud_gateway_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->update_nva_security_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_gateway_name** | **str**| Cloud gateway name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update NVA security Rules | [optional]

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

# **validate_account_add**
> validate_account_add()



Authenticate cloud account credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud account info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_account_add(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_account_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud account info | [optional]

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

# **validate_account_update_credentials**
> validate_account_update_credentials(account_id)



Update multicloud account credential

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Account Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud account info (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.validate_account_update_credentials(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_account_update_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_account_update_credentials(account_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_account_update_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud account info | [optional]

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

# **validate_edge_account_add**
> validate_edge_account_add()



Authenticate edge account credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud edge account info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_edge_account_add(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_edge_account_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud edge account info | [optional]

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

# **validate_edge_account_update_credentials**
> validate_edge_account_update_credentials(account_id)



Update Multicloud edge account credential

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multi_cloud_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multi_cloud_api.ConfigurationMultiCloudApi(api_client)
    account_id = "accountId_example" # str | Multicloud Edge Account Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Multicloud edge account info (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.validate_edge_account_update_credentials(account_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_edge_account_update_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_edge_account_update_credentials(account_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultiCloudApi->validate_edge_account_update_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Multicloud Edge Account Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Multicloud edge account info | [optional]

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

