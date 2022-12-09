# openapi_client.ConfigurationFeatureProfileSDWANApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cedge_service_profile_switchport_parcel_restful_resource**](ConfigurationFeatureProfileSDWANApi.md#cedge_service_profile_switchport_parcel_restful_resource) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/switchport | 
[**create_aaa_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_aaa_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/aaa | 
[**create_banner_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_banner_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/banner | 
[**create_basic_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_basic_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/basic | 
[**create_bfd_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_bfd_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/bfd | 
[**create_cellular_controller_and_cellular_profile_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_cellular_controller_and_cellular_profile_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile | 
[**create_cellular_controller_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_cellular_controller_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller | 
[**create_cellular_profile_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_cellular_profile_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/cellular-profile | 
[**create_dhcp_server_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_dhcp_server_profile_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/dhcp-server | 
[**create_global_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_global_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/global | 
[**create_lan_vpn_and_routing_bgp_parcel_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_and_routing_bgp_parcel_association_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp | 
[**create_lan_vpn_and_routing_ospf_parcel_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_and_routing_ospf_parcel_association_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf | 
[**create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/dhcp-server | 
[**create_lan_vpn_interface_ethernet_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_interface_ethernet_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet | 
[**create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/svi/{sviId}/dhcp-server | 
[**create_lan_vpn_interface_svi_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_interface_svi_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi | 
[**create_lan_vpn_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_lan_vpn_profile_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn | 
[**create_logging_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_logging_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/logging | 
[**create_management_vpn_interface_ethernet_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_management_vpn_interface_ethernet_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet | 
[**create_management_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_management_vpn_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn | 
[**create_ntp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_ntp_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/ntp | 
[**create_omp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_omp_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/omp | 
[**create_routing_bgp_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_routing_bgp_profile_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/routing/bgp | 
[**create_routing_bgp_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_routing_bgp_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/routing/bgp | 
[**create_routing_ospf_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_routing_ospf_profile_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/routing/ospf | 
[**create_sdwan_config_profile_parcel_for_cli**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_config_profile_parcel_for_cli) | **POST** /v1/feature-profile/sdwan/cli/{cliId}/config | 
[**create_sdwan_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_feature_profile) | **POST** /v1/feature-profile/sdwan/cli | 
[**create_sdwan_other_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_other_feature_profile) | **POST** /v1/feature-profile/sdwan/other | 
[**create_sdwan_service_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_service_feature_profile) | **POST** /v1/feature-profile/sdwan/service | 
[**create_sdwan_system_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_system_feature_profile) | **POST** /v1/feature-profile/sdwan/system | 
[**create_sdwan_transport_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#create_sdwan_transport_feature_profile) | **POST** /v1/feature-profile/sdwan/transport | 
[**create_snmp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#create_snmp_profile_parcel_for_system) | **POST** /v1/feature-profile/sdwan/system/{systemId}/snmp | 
[**create_thousandeyes_profile_parcel_for_other**](ConfigurationFeatureProfileSDWANApi.md#create_thousandeyes_profile_parcel_for_other) | **POST** /v1/feature-profile/sdwan/other/{otherId}/thousandeyes | 
[**create_tracker_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_tracker_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/tracker | 
[**create_wan_vpn_and_routing_bgp_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_and_routing_bgp_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp | 
[**create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/tracker | 
[**create_wan_vpn_interface_cellular_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_interface_cellular_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular | 
[**create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/tracker | 
[**create_wan_vpn_interface_ethernet_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_interface_ethernet_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet | 
[**create_wan_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#create_wan_vpn_profile_parcel_for_transport) | **POST** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn | 
[**create_wirelesslan_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#create_wirelesslan_profile_parcel_for_service) | **POST** /v1/feature-profile/sdwan/service/{serviceId}/wirelesslan | 
[**delete_aaa_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_aaa_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId} | 
[**delete_banner_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_banner_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId} | 
[**delete_basic_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_basic_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/basic/{basicId} | 
[**delete_bfd_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_bfd_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId} | 
[**delete_cellular_controller_and_cellular_profile_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_cellular_controller_and_cellular_profile_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId} | 
[**delete_cellular_controller_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_cellular_controller_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId} | 
[**delete_cellular_profile_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_cellular_profile_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId} | 
[**delete_config_profile_parcel_for_cli**](ConfigurationFeatureProfileSDWANApi.md#delete_config_profile_parcel_for_cli) | **DELETE** /v1/feature-profile/sdwan/cli/{cliId}/config/{configId} | 
[**delete_dhcp_server_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_dhcp_server_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId} | 
[**delete_global_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_global_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/global/{globalId} | 
[**delete_lan_vpn_and_routing_bgp_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_and_routing_bgp_association_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**delete_lan_vpn_and_routing_ospf_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_and_routing_ospf_association_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId} | 
[**delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId} | 
[**delete_lan_vpn_interface_ethernet_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_interface_ethernet_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId} | 
[**delete_lan_vpn_interface_svi_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_interface_svi_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId} | 
[**delete_lan_vpn_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_lan_vpn_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId} | 
[**delete_logging_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_logging_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId} | 
[**delete_management_vpn_interface_ethernet_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_management_vpn_interface_ethernet_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**delete_management_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_management_vpn_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId} | 
[**delete_ntp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_ntp_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId} | 
[**delete_omp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_omp_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/omp/{ompId} | 
[**delete_routing_bgp_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_routing_bgp_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId} | 
[**delete_routing_bgp_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_routing_bgp_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId} | 
[**delete_routing_ospf_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_routing_ospf_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId} | 
[**delete_sdwan_feature_profile_for_cli**](ConfigurationFeatureProfileSDWANApi.md#delete_sdwan_feature_profile_for_cli) | **DELETE** /v1/feature-profile/sdwan/cli/{cliId} | 
[**delete_sdwan_other_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#delete_sdwan_other_feature_profile) | **DELETE** /v1/feature-profile/sdwan/other/{otherId} | 
[**delete_sdwan_service_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#delete_sdwan_service_feature_profile) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId} | 
[**delete_sdwan_system_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#delete_sdwan_system_feature_profile) | **DELETE** /v1/feature-profile/sdwan/system/{systemId} | 
[**delete_sdwan_transport_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#delete_sdwan_transport_feature_profile) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId} | 
[**delete_snmp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#delete_snmp_profile_parcel_for_system) | **DELETE** /v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId} | 
[**delete_switchport_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_switchport_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId} | 
[**delete_thousandeyes_profile_parcel_for_other**](ConfigurationFeatureProfileSDWANApi.md#delete_thousandeyes_profile_parcel_for_other) | **DELETE** /v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId} | 
[**delete_tracker_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_tracker_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId} | 
[**delete_wan_vpn_and_routing_bgp_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_and_routing_bgp_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**delete_wan_vpn_interface_cellular_and_tracker_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_interface_cellular_and_tracker_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/tracker/{trackerId} | 
[**delete_wan_vpn_interface_cellular_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_interface_cellular_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId} | 
[**delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId} | 
[**delete_wan_vpn_interface_ethernet_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_interface_ethernet_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**delete_wan_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#delete_wan_vpn_profile_parcel_for_transport) | **DELETE** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId} | 
[**delete_wirelesslan_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#delete_wirelesslan_profile_parcel_for_service) | **DELETE** /v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId} | 
[**edit_aaa_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_aaa_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId} | 
[**edit_banner_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_banner_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId} | 
[**edit_basic_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_basic_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/basic/{basicId} | 
[**edit_bfd_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_bfd_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId} | 
[**edit_cellular_controller_and_cellular_profile_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_cellular_controller_and_cellular_profile_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId} | 
[**edit_cellular_controller_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_cellular_controller_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId} | 
[**edit_cellular_profile_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_cellular_profile_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId} | 
[**edit_config_profile_parcel_for_cli**](ConfigurationFeatureProfileSDWANApi.md#edit_config_profile_parcel_for_cli) | **PUT** /v1/feature-profile/sdwan/cli/{cliId}/config/{configId} | 
[**edit_dhcp_server_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_dhcp_server_profile_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId} | 
[**edit_global_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_global_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/global/{globalId} | 
[**edit_lan_vpn_and_routing_bgp_parcel_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_and_routing_bgp_parcel_association_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**edit_lan_vpn_and_routing_ospf_parcel_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_and_routing_ospf_parcel_association_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId} | 
[**edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId} | 
[**edit_lan_vpn_interface_ethernet_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_interface_ethernet_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId} | 
[**edit_lan_vpn_interface_svi_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_interface_svi_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId} | 
[**edit_lan_vpn_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_lan_vpn_profile_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId} | 
[**edit_logging_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_logging_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId} | 
[**edit_management_vpn_interface_ethernet_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_management_vpn_interface_ethernet_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**edit_management_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_management_vpn_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId} | 
[**edit_ntp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_ntp_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId} | 
[**edit_omp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_omp_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/omp/{ompId} | 
[**edit_routing_bgp_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_routing_bgp_profile_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId} | 
[**edit_routing_bgp_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_routing_bgp_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId} | 
[**edit_routing_ospf_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_routing_ospf_profile_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId} | 
[**edit_sdwan_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#edit_sdwan_feature_profile) | **PUT** /v1/feature-profile/sdwan/cli/{cliId} | 
[**edit_sdwan_other_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#edit_sdwan_other_feature_profile) | **PUT** /v1/feature-profile/sdwan/other/{otherId} | 
[**edit_sdwan_service_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#edit_sdwan_service_feature_profile) | **PUT** /v1/feature-profile/sdwan/service/{serviceId} | 
[**edit_sdwan_system_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#edit_sdwan_system_feature_profile) | **PUT** /v1/feature-profile/sdwan/system/{systemId} | 
[**edit_sdwan_transport_feature_profile**](ConfigurationFeatureProfileSDWANApi.md#edit_sdwan_transport_feature_profile) | **PUT** /v1/feature-profile/sdwan/transport/{transportId} | 
[**edit_snmp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#edit_snmp_profile_parcel_for_system) | **PUT** /v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId} | 
[**edit_switchport_parcel_association_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_switchport_parcel_association_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId} | 
[**edit_thousandeyes_profile_parcel_for_other**](ConfigurationFeatureProfileSDWANApi.md#edit_thousandeyes_profile_parcel_for_other) | **PUT** /v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId} | 
[**edit_tracker_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_tracker_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId} | 
[**edit_wan_vpn_and_routing_bgp_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_and_routing_bgp_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/tracker/{trackerId} | 
[**edit_wan_vpn_interface_cellular_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_interface_cellular_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId} | 
[**edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId} | 
[**edit_wan_vpn_interface_ethernet_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_interface_ethernet_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**edit_wan_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#edit_wan_vpn_profile_parcel_for_transport) | **PUT** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId} | 
[**edit_wirelesslan_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#edit_wirelesslan_profile_parcel_for_service) | **PUT** /v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId} | 
[**get_aaa_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_aaa_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId} | 
[**get_aaa_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_aaa_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/aaa | 
[**get_banner_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_banner_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId} | 
[**get_banner_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_banner_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/banner | 
[**get_basic_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_basic_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/basic/{basicId} | 
[**get_basic_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_basic_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/basic | 
[**get_bfd_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_bfd_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId} | 
[**get_bfd_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_bfd_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/bfd | 
[**get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema**](ConfigurationFeatureProfileSDWANApi.md#get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema) | **GET** /v1/feature-profile/sdwan/service/lan/vpn/interface/svi/schema | 
[**get_cedge_service_switchport_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_cedge_service_switchport_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/switchport/schema | 
[**get_cedge_system_global_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_cedge_system_global_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/global/schema | 
[**get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId} | 
[**get_cellular_controller_associated_cellular_profile_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_controller_associated_cellular_profile_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile | 
[**get_cellular_controller_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_controller_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId} | 
[**get_cellular_controller_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_controller_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller | 
[**get_cellular_profile_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_profile_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId} | 
[**get_cellular_profile_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_cellular_profile_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/cellular-profile | 
[**get_config_profile_parcel_by_parcel_id_for_cli**](ConfigurationFeatureProfileSDWANApi.md#get_config_profile_parcel_by_parcel_id_for_cli) | **GET** /v1/feature-profile/sdwan/cli/{cliId}/config/{configId} | 
[**get_config_profile_parcel_for_cli**](ConfigurationFeatureProfileSDWANApi.md#get_config_profile_parcel_for_cli) | **GET** /v1/feature-profile/sdwan/cli/{cliId}/config | 
[**get_dhcp_server_profile_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_dhcp_server_profile_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId} | 
[**get_dhcp_server_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_dhcp_server_profile_parcel_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/dhcp-server | 
[**get_global_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_global_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/global/{globalId} | 
[**get_global_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_global_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/global | 
[**get_interface_cellular_parcels_for_transport_wan_vpn**](ConfigurationFeatureProfileSDWANApi.md#get_interface_cellular_parcels_for_transport_wan_vpn) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular | 
[**get_interface_ethernet_parcels_for_service_lan_vpn**](ConfigurationFeatureProfileSDWANApi.md#get_interface_ethernet_parcels_for_service_lan_vpn) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet | 
[**get_interface_ethernet_parcels_for_transport_management_vpn**](ConfigurationFeatureProfileSDWANApi.md#get_interface_ethernet_parcels_for_transport_management_vpn) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet | 
[**get_interface_ethernet_parcels_for_transport_wan_vpn**](ConfigurationFeatureProfileSDWANApi.md#get_interface_ethernet_parcels_for_transport_wan_vpn) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet | 
[**get_interface_svi_parcels_for_service_lan_vpn**](ConfigurationFeatureProfileSDWANApi.md#get_interface_svi_parcels_for_service_lan_vpn) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi | 
[**get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**get_lan_vpn_associated_routing_bgp_parcels_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_associated_routing_bgp_parcels_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp | 
[**get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId} | 
[**get_lan_vpn_associated_routing_ospf_parcels_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_associated_routing_ospf_parcels_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf | 
[**get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId} | 
[**get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/dhcp-server | 
[**get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId} | 
[**get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server | 
[**get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId} | 
[**get_lan_vpn_profile_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_profile_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId} | 
[**get_lan_vpn_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_lan_vpn_profile_parcel_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn | 
[**get_logging_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_logging_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId} | 
[**get_logging_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_logging_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/logging | 
[**get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**get_management_vpn_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_management_vpn_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId} | 
[**get_management_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_management_vpn_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/management/vpn | 
[**get_ntp_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_ntp_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId} | 
[**get_ntp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_ntp_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/ntp | 
[**get_omp_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_omp_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/omp/{ompId} | 
[**get_omp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_omp_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/omp | 
[**get_routing_bgp_profile_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_routing_bgp_profile_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId} | 
[**get_routing_bgp_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_routing_bgp_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId} | 
[**get_routing_bgp_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_routing_bgp_profile_parcel_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/routing/bgp | 
[**get_routing_bgp_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_routing_bgp_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/routing/bgp | 
[**get_routing_ospf_profile_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_routing_ospf_profile_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId} | 
[**get_routing_ospf_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_routing_ospf_profile_parcel_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/routing/ospf | 
[**get_sdwan_feature_profile_by_profile_id**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_feature_profile_by_profile_id) | **GET** /v1/feature-profile/sdwan/cli/{cliId} | 
[**get_sdwan_feature_profile_by_sdwan_family**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_feature_profile_by_sdwan_family) | **GET** /v1/feature-profile/sdwan | 
[**get_sdwan_feature_profiles_by_family_and_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_feature_profiles_by_family_and_type) | **GET** /v1/feature-profile/sdwan/cli | 
[**get_sdwan_other_feature_profile_by_profile_id**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_other_feature_profile_by_profile_id) | **GET** /v1/feature-profile/sdwan/other/{otherId} | 
[**get_sdwan_other_feature_profiles**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_other_feature_profiles) | **GET** /v1/feature-profile/sdwan/other | 
[**get_sdwan_other_thousandeyes_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_other_thousandeyes_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/other/thousandeyes/schema | 
[**get_sdwan_service_dhcp_server_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_dhcp_server_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/dhcp-server/schema | 
[**get_sdwan_service_feature_profile_by_profile_id**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_feature_profile_by_profile_id) | **GET** /v1/feature-profile/sdwan/service/{serviceId} | 
[**get_sdwan_service_feature_profiles**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_feature_profiles) | **GET** /v1/feature-profile/sdwan/service | 
[**get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema) | **GET** /v1/feature-profile/sdwan/service/lan/vpn/interface/ethernet/schema | 
[**get_sdwan_service_lan_vpn_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_lan_vpn_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/lan/vpn/schema | 
[**get_sdwan_service_routing_bgp_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_routing_bgp_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/routing/bgp/schema | 
[**get_sdwan_service_routing_ospf_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_routing_ospf_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/routing/ospf/schema | 
[**get_sdwan_service_wirelesslan_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_service_wirelesslan_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/service/wirelesslan/schema | 
[**get_sdwan_system_aaa_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_aaa_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/aaa/schema | 
[**get_sdwan_system_banner_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_banner_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/banner/schema | 
[**get_sdwan_system_basic_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_basic_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/basic/schema | 
[**get_sdwan_system_bfd_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_bfd_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/bfd/schema | 
[**get_sdwan_system_feature_profile_by_profile_id**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_feature_profile_by_profile_id) | **GET** /v1/feature-profile/sdwan/system/{systemId} | 
[**get_sdwan_system_feature_profiles**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_feature_profiles) | **GET** /v1/feature-profile/sdwan/system | 
[**get_sdwan_system_logging_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_logging_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/logging/schema | 
[**get_sdwan_system_ntp_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_ntp_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/ntp/schema | 
[**get_sdwan_system_omp_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_omp_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/omp/schema | 
[**get_sdwan_system_snmp_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_system_snmp_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/system/snmp/schema | 
[**get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/cellular-controller/schema | 
[**get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/cellular-profile/schema | 
[**get_sdwan_transport_feature_profile_by_profile_id**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_feature_profile_by_profile_id) | **GET** /v1/feature-profile/sdwan/transport/{transportId} | 
[**get_sdwan_transport_feature_profiles**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_feature_profiles) | **GET** /v1/feature-profile/sdwan/transport | 
[**get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema) | **GET** /v1/feature-profile/sdwan/transport/management/vpn/interface/ethernet/schema | 
[**get_sdwan_transport_management_vpn_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_management_vpn_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/management/vpn/schema | 
[**get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/routing/bgp/schema | 
[**get_sdwan_transport_tracker_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_tracker_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/tracker/schema | 
[**get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema) | **GET** /v1/feature-profile/sdwan/transport/wan/vpn/interface/cellular/schema | 
[**get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema) | **GET** /v1/feature-profile/sdwan/transport/wan/vpn/interface/ethernet/schema | 
[**get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type**](ConfigurationFeatureProfileSDWANApi.md#get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type) | **GET** /v1/feature-profile/sdwan/transport/wan/vpn/schema | 
[**get_snmp_profile_parcel_by_parcel_id_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_snmp_profile_parcel_by_parcel_id_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/snmp/{snmpId} | 
[**get_snmp_profile_parcel_for_system**](ConfigurationFeatureProfileSDWANApi.md#get_snmp_profile_parcel_for_system) | **GET** /v1/feature-profile/sdwan/system/{systemId}/snmp | 
[**get_switchport_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_switchport_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId} | 
[**get_switchport_parcels_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_switchport_parcels_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/switchport | 
[**get_thousandeyes_profile_parcel_by_parcel_id_for_other**](ConfigurationFeatureProfileSDWANApi.md#get_thousandeyes_profile_parcel_by_parcel_id_for_other) | **GET** /v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId} | 
[**get_thousandeyes_profile_parcel_for_other**](ConfigurationFeatureProfileSDWANApi.md#get_thousandeyes_profile_parcel_for_other) | **GET** /v1/feature-profile/sdwan/other/{otherId}/thousandeyes | 
[**get_tracker_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_tracker_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId} | 
[**get_tracker_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_tracker_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/tracker | 
[**get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId} | 
[**get_wan_vpn_associated_routing_bgp_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_associated_routing_bgp_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp | 
[**get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/tracker/{trackerId} | 
[**get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/tracker | 
[**get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId} | 
[**get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId} | 
[**get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker | 
[**get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId} | 
[**get_wan_vpn_profile_parcel_by_parcel_id_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_profile_parcel_by_parcel_id_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId} | 
[**get_wan_vpn_profile_parcel_for_transport**](ConfigurationFeatureProfileSDWANApi.md#get_wan_vpn_profile_parcel_for_transport) | **GET** /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn | 
[**get_wirelesslan_profile_parcel_by_parcel_id_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_wirelesslan_profile_parcel_by_parcel_id_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId} | 
[**get_wirelesslan_profile_parcel_for_service**](ConfigurationFeatureProfileSDWANApi.md#get_wirelesslan_profile_parcel_for_service) | **GET** /v1/feature-profile/sdwan/service/{serviceId}/wirelesslan | 


# **cedge_service_profile_switchport_parcel_restful_resource**
> str cedge_service_profile_switchport_parcel_restful_resource(service_id)



Create a switchport Parcel to a service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Feature Profile Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cedge_service_profile_switchport_parcel_restful_resource(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->cedge_service_profile_switchport_parcel_restful_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.cedge_service_profile_switchport_parcel_restful_resource(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->cedge_service_profile_switchport_parcel_restful_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Feature Profile Id | [optional]

### Return type

**str**

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

# **create_aaa_profile_parcel_for_system**
> str create_aaa_profile_parcel_for_system(system_id)



Create a Aaa Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Aaa Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_aaa_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_aaa_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_aaa_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_aaa_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Aaa Profile Parcel | [optional]

### Return type

**str**

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

# **create_banner_profile_parcel_for_system**
> str create_banner_profile_parcel_for_system(system_id)



Create a Banner Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Banner Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_banner_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_banner_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_banner_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_banner_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Banner Profile Parcel | [optional]

### Return type

**str**

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

# **create_basic_profile_parcel_for_system**
> str create_basic_profile_parcel_for_system(system_id)



Create a Basic Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Basic Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_basic_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_basic_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_basic_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_basic_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Basic Profile Parcel | [optional]

### Return type

**str**

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

# **create_bfd_profile_parcel_for_system**
> str create_bfd_profile_parcel_for_system(system_id)



Create a Bfd Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Bfd Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bfd_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_bfd_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bfd_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_bfd_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Bfd Profile Parcel | [optional]

### Return type

**str**

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

# **create_cellular_controller_and_cellular_profile_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id)



Associate a cellularcontroller parcel with a cellularprofile Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Cellular Controller Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Profile Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_controller_and_cellular_profile_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_controller_and_cellular_profile_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Cellular Controller Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Profile Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_cellular_controller_profile_parcel_for_transport**
> str create_cellular_controller_profile_parcel_for_transport(transport_id)



Create a Cellular Controller Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Controller Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cellular_controller_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_controller_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cellular_controller_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_controller_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Controller Profile Parcel | [optional]

### Return type

**str**

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

# **create_cellular_profile_profile_parcel_for_transport**
> str create_cellular_profile_profile_parcel_for_transport(transport_id)



Create a Cellular Profile Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Profile Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cellular_profile_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_profile_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cellular_profile_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_cellular_profile_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Profile Profile Parcel | [optional]

### Return type

**str**

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

# **create_dhcp_server_profile_parcel_for_service**
> str create_dhcp_server_profile_parcel_for_service(service_id)



Create a Dhcp Server Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Dhcp Server Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dhcp_server_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_dhcp_server_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dhcp_server_profile_parcel_for_service(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_dhcp_server_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Dhcp Server Profile Parcel | [optional]

### Return type

**str**

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

# **create_global_profile_parcel_for_system**
> str create_global_profile_parcel_for_system(system_id)



Create a Global Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Global Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_global_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_global_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_global_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_global_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Global Profile Parcel | [optional]

### Return type

**str**

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

# **create_lan_vpn_and_routing_bgp_parcel_association_for_service**
> bool, date, datetime, dict, float, int, list, str, none_type create_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id)



Associate a lanvpn parcel with a routingbgp Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Lan Vpn Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_and_routing_bgp_parcel_association_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_and_routing_bgp_parcel_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Lan Vpn Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_lan_vpn_and_routing_ospf_parcel_association_for_service**
> bool, date, datetime, dict, float, int, list, str, none_type create_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id)



Associate a lanvpn parcel with a routingospf Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Lan Vpn Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Ospf Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_and_routing_ospf_parcel_association_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_and_routing_ospf_parcel_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Lan Vpn Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Ospf Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, ethernet_id)



Associate a LanVpnInterfaceEthernet parcel with a DhcpServer Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_parcel_id = "vpnParcelId_example" # str | VPN Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | DhcpServer Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, ethernet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_parcel_id** | **str**| VPN Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| DhcpServer Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_lan_vpn_interface_ethernet_parcel_for_service**
> str create_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id)



Create a LanVpn InterfaceEthernet parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_ethernet_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_ethernet_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, svi_id)



Associate a LanVpnInterfaceSvi parcel with a DhcpServer Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_parcel_id = "vpnParcelId_example" # str | VPN Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | DhcpServer Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, svi_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_parcel_id, svi_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_parcel_id** | **str**| VPN Profile Parcel ID |
 **svi_id** | **str**| Interface Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| DhcpServer Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_lan_vpn_interface_svi_parcel_for_service**
> str create_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id)



Create a LanVpn InterfaceSvi parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Interface Svi Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_svi_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_interface_svi_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Interface Svi Profile Parcel | [optional]

### Return type

**str**

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

# **create_lan_vpn_profile_parcel_for_service**
> str create_lan_vpn_profile_parcel_for_service(service_id)



Create a Lan Vpn Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_lan_vpn_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lan_vpn_profile_parcel_for_service(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_lan_vpn_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **create_logging_profile_parcel_for_system**
> str create_logging_profile_parcel_for_system(system_id)



Create a Logging Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Logging Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_logging_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_logging_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_logging_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_logging_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Logging Profile Parcel | [optional]

### Return type

**str**

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

# **create_management_vpn_interface_ethernet_parcel_for_transport**
> str create_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id)



Create a ManagementVpn InterfaceEthernet parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Management Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_management_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_management_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Management Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **create_management_vpn_profile_parcel_for_transport**
> str create_management_vpn_profile_parcel_for_transport(transport_id)



Create a Management Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Management Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_management_vpn_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_management_vpn_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_management_vpn_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_management_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Management Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **create_ntp_profile_parcel_for_system**
> str create_ntp_profile_parcel_for_system(system_id)



Create a Ntp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Ntp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ntp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_ntp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ntp_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_ntp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Ntp Profile Parcel | [optional]

### Return type

**str**

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

# **create_omp_profile_parcel_for_system**
> str create_omp_profile_parcel_for_system(system_id)



Create a Omp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Omp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_omp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_omp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_omp_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_omp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Omp Profile Parcel | [optional]

### Return type

**str**

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

# **create_routing_bgp_profile_parcel_for_service**
> str create_routing_bgp_profile_parcel_for_service(service_id)



Create a Routing Bgp Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_routing_bgp_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_bgp_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_routing_bgp_profile_parcel_for_service(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_bgp_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**str**

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

# **create_routing_bgp_profile_parcel_for_transport**
> str create_routing_bgp_profile_parcel_for_transport(transport_id)



Create a Routing Bgp Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_routing_bgp_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_bgp_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_routing_bgp_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_bgp_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**str**

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

# **create_routing_ospf_profile_parcel_for_service**
> str create_routing_ospf_profile_parcel_for_service(service_id)



Create a Routing Ospf Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Ospf Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_routing_ospf_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_ospf_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_routing_ospf_profile_parcel_for_service(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_routing_ospf_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Ospf Profile Parcel | [optional]

### Return type

**str**

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

# **create_sdwan_config_profile_parcel_for_cli**
> str create_sdwan_config_profile_parcel_for_cli(cli_id)



Create a config Profile Parcel for cli feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | cli config Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sdwan_config_profile_parcel_for_cli(cli_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_config_profile_parcel_for_cli: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_config_profile_parcel_for_cli(cli_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_config_profile_parcel_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| cli config Profile Parcel | [optional]

### Return type

**str**

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

# **create_sdwan_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type create_sdwan_feature_profile()



Create a SDWAN  Feature Profile with profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_feature_profile(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_sdwan_other_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type create_sdwan_other_feature_profile()



Create a SDWAN Other Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_other_feature_profile(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_other_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_sdwan_service_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type create_sdwan_service_feature_profile()



Create a SDWAN Service Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_service_feature_profile(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_service_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_sdwan_system_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type create_sdwan_system_feature_profile()



Create a SDWAN System Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_system_feature_profile(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_system_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_sdwan_transport_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type create_sdwan_transport_feature_profile()



Create a SDWAN Transport Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sdwan_transport_feature_profile(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_sdwan_transport_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_snmp_profile_parcel_for_system**
> str create_snmp_profile_parcel_for_system(system_id)



Create a Snmp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Snmp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_snmp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_snmp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_snmp_profile_parcel_for_system(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_snmp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Snmp Profile Parcel | [optional]

### Return type

**str**

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

# **create_thousandeyes_profile_parcel_for_other**
> str create_thousandeyes_profile_parcel_for_other(other_id)



Create a Thousandeyes Profile Parcel for Other feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Thousandeyes Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_thousandeyes_profile_parcel_for_other(other_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_thousandeyes_profile_parcel_for_other: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_thousandeyes_profile_parcel_for_other(other_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_thousandeyes_profile_parcel_for_other: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Thousandeyes Profile Parcel | [optional]

### Return type

**str**

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

# **create_tracker_profile_parcel_for_transport**
> str create_tracker_profile_parcel_for_transport(transport_id)



Create a Tracker Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tracker_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_tracker_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tracker_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_tracker_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel | [optional]

### Return type

**str**

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

# **create_wan_vpn_and_routing_bgp_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id)



Associate a wanvpn parcel with a routingbgp Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Wan Vpn Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_and_routing_bgp_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_and_routing_bgp_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Wan Vpn Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, cellular_id)



Associate a WanVpnInterfaceCellular parcel with a Tracker Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_parcel_id = "vpnParcelId_example" # str | VPN Profile Parcel ID
    cellular_id = "cellularId_example" # str | Interface Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, cellular_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, cellular_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_parcel_id** | **str**| VPN Profile Parcel ID |
 **cellular_id** | **str**| Interface Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_wan_vpn_interface_cellular_parcel_for_transport**
> str create_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id)



Create a wanvpn Cellular interface Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | VPN Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | WanVpn Interface Cellular Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_cellular_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_cellular_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| VPN Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| WanVpn Interface Cellular Profile Parcel | [optional]

### Return type

**str**

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

# **create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, ethernet_id)



Associate a WanVpnInterfaceEthernet parcel with a Tracker Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_parcel_id = "vpnParcelId_example" # str | VPN Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_parcel_id, ethernet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_parcel_id** | **str**| VPN Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel Id | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_wan_vpn_interface_ethernet_parcel_for_transport**
> str create_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id)



Create a WanVpn InterfaceEthernet parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wan Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wan Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **create_wan_vpn_profile_parcel_for_transport**
> str create_wan_vpn_profile_parcel_for_transport(transport_id)



Create a Wan Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wan Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_vpn_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wan_vpn_profile_parcel_for_transport(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wan_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wan Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **create_wirelesslan_profile_parcel_for_service**
> str create_wirelesslan_profile_parcel_for_service(service_id)



Create a Wirelesslan Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wirelesslan Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wirelesslan_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wirelesslan_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_wirelesslan_profile_parcel_for_service(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->create_wirelesslan_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wirelesslan Profile Parcel | [optional]

### Return type

**str**

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

# **delete_aaa_profile_parcel_for_system**
> delete_aaa_profile_parcel_for_system(system_id, aaa_id)



Delete a Aaa Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    aaa_id = "aaaId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_aaa_profile_parcel_for_system(system_id, aaa_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_aaa_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **aaa_id** | **str**| Profile Parcel ID |

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

# **delete_banner_profile_parcel_for_system**
> delete_banner_profile_parcel_for_system(system_id, banner_id)



Delete a Banner Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    banner_id = "bannerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_banner_profile_parcel_for_system(system_id, banner_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_banner_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **banner_id** | **str**| Profile Parcel ID |

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

# **delete_basic_profile_parcel_for_system**
> delete_basic_profile_parcel_for_system(system_id, basic_id)



Delete a Basic Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    basic_id = "basicId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_basic_profile_parcel_for_system(system_id, basic_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_basic_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **basic_id** | **str**| Profile Parcel ID |

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

# **delete_bfd_profile_parcel_for_system**
> delete_bfd_profile_parcel_for_system(system_id, bfd_id)



Delete a Bfd Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    bfd_id = "bfdId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_bfd_profile_parcel_for_system(system_id, bfd_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_bfd_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **bfd_id** | **str**| Profile Parcel ID |

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

# **delete_cellular_controller_and_cellular_profile_association_for_transport**
> delete_cellular_controller_and_cellular_profile_association_for_transport(transport_id, cellular_controller_id, cellular_profile_id)



Delete a CellularController parcel and a CellularProfile Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID
    cellular_profile_id = "cellularProfileId_example" # str | Cellular Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cellular_controller_and_cellular_profile_association_for_transport(transport_id, cellular_controller_id, cellular_profile_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_cellular_controller_and_cellular_profile_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |
 **cellular_profile_id** | **str**| Cellular Profile Parcel ID |

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

# **delete_cellular_controller_profile_parcel_for_transport**
> delete_cellular_controller_profile_parcel_for_transport(transport_id, cellular_controller_id)



Delete a Cellular Controller Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cellular_controller_profile_parcel_for_transport(transport_id, cellular_controller_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_cellular_controller_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |

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

# **delete_cellular_profile_profile_parcel_for_transport**
> delete_cellular_profile_profile_parcel_for_transport(transport_id, cellular_profile_id)



Delete a Cellular Profile Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_profile_id = "cellularProfileId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cellular_profile_profile_parcel_for_transport(transport_id, cellular_profile_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_cellular_profile_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_profile_id** | **str**| Profile Parcel ID |

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

# **delete_config_profile_parcel_for_cli**
> delete_config_profile_parcel_for_cli(cli_id, config_id)



Delete a config Profile Parcel for cli feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile ID
    config_id = "configId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_config_profile_parcel_for_cli(cli_id, config_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_config_profile_parcel_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile ID |
 **config_id** | **str**| Profile Parcel ID |

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

# **delete_dhcp_server_profile_parcel_for_service**
> delete_dhcp_server_profile_parcel_for_service(service_id, dhcp_server_id)



Delete a Dhcp Server Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    dhcp_server_id = "dhcpServerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_dhcp_server_profile_parcel_for_service(service_id, dhcp_server_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_dhcp_server_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **dhcp_server_id** | **str**| Profile Parcel ID |

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

# **delete_global_profile_parcel_for_system**
> delete_global_profile_parcel_for_system(system_id, global_id)



Delete a Global Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    global_id = "globalId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_global_profile_parcel_for_system(system_id, global_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_global_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **global_id** | **str**| Profile Parcel ID |

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

# **delete_lan_vpn_and_routing_bgp_association_for_service**
> delete_lan_vpn_and_routing_bgp_association_for_service(service_id, vpn_id, bgp_id)



Delete a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_and_routing_bgp_association_for_service(service_id, vpn_id, bgp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_and_routing_bgp_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp Parcel ID |

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

# **delete_lan_vpn_and_routing_ospf_association_for_service**
> delete_lan_vpn_and_routing_ospf_association_for_service(service_id, vpn_id, ospf_id)



Delete a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ospf_id = "ospfId_example" # str | Routing Ospf Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_and_routing_ospf_association_for_service(service_id, vpn_id, ospf_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_and_routing_ospf_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ospf_id** | **str**| Routing Ospf Parcel ID |

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

# **delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport**
> delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)



Delete a LanVpnInterfaceEthernet and a DhcpServer Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_interface_ethernet_and_dhcp_server_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer Parcel ID |

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

# **delete_lan_vpn_interface_ethernet_for_service**
> delete_lan_vpn_interface_ethernet_for_service(service_id, vpn_id, ethernet_id)



Delete a  LanVpn InterfaceEthernet Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_interface_ethernet_for_service(service_id, vpn_id, ethernet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_interface_ethernet_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

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

# **delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport**
> delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)



Delete a LanVpnInterfaceSvi and a DhcpServer Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer Parcel ID |

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

# **delete_lan_vpn_interface_svi_for_service**
> delete_lan_vpn_interface_svi_for_service(service_id, vpn_id, svi_id)



Delete a  LanVpn InterfaceSvi Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_interface_svi_for_service(service_id, vpn_id, svi_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_interface_svi_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface Parcel ID |

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

# **delete_lan_vpn_profile_parcel_for_service**
> delete_lan_vpn_profile_parcel_for_service(service_id, vpn_id)



Delete a Lan Vpn Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_lan_vpn_profile_parcel_for_service(service_id, vpn_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_lan_vpn_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

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

# **delete_logging_profile_parcel_for_system**
> delete_logging_profile_parcel_for_system(system_id, logging_id)



Delete a Logging Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    logging_id = "loggingId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_logging_profile_parcel_for_system(system_id, logging_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_logging_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **logging_id** | **str**| Profile Parcel ID |

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

# **delete_management_vpn_interface_ethernet_for_transport**
> delete_management_vpn_interface_ethernet_for_transport(transport_id, vpn_id, ethernet_id)



Delete a  ManagementVpn InterfaceEthernet Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_management_vpn_interface_ethernet_for_transport(transport_id, vpn_id, ethernet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_management_vpn_interface_ethernet_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

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

# **delete_management_vpn_profile_parcel_for_transport**
> delete_management_vpn_profile_parcel_for_transport(transport_id, vpn_id)



Delete a Management Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_management_vpn_profile_parcel_for_transport(transport_id, vpn_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_management_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

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

# **delete_ntp_profile_parcel_for_system**
> delete_ntp_profile_parcel_for_system(system_id, ntp_id)



Delete a Ntp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    ntp_id = "ntpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ntp_profile_parcel_for_system(system_id, ntp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_ntp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **ntp_id** | **str**| Profile Parcel ID |

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

# **delete_omp_profile_parcel_for_system**
> delete_omp_profile_parcel_for_system(system_id, omp_id)



Delete a Omp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    omp_id = "ompId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_omp_profile_parcel_for_system(system_id, omp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_omp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **omp_id** | **str**| Profile Parcel ID |

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

# **delete_routing_bgp_profile_parcel_for_service**
> delete_routing_bgp_profile_parcel_for_service(service_id, bgp_id)



Delete a Routing Bgp Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_routing_bgp_profile_parcel_for_service(service_id, bgp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_routing_bgp_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |

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

# **delete_routing_bgp_profile_parcel_for_transport**
> delete_routing_bgp_profile_parcel_for_transport(transport_id, bgp_id)



Delete a Routing Bgp Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_routing_bgp_profile_parcel_for_transport(transport_id, bgp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_routing_bgp_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |

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

# **delete_routing_ospf_profile_parcel_for_service**
> delete_routing_ospf_profile_parcel_for_service(service_id, ospf_id)



Delete a Routing Ospf Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    ospf_id = "ospfId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_routing_ospf_profile_parcel_for_service(service_id, ospf_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_routing_ospf_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **ospf_id** | **str**| Profile Parcel ID |

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

# **delete_sdwan_feature_profile_for_cli**
> delete_sdwan_feature_profile_for_cli(cli_id)



Delete Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sdwan_feature_profile_for_cli(cli_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_sdwan_feature_profile_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**|  |

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

# **delete_sdwan_other_feature_profile**
> delete_sdwan_other_feature_profile(other_id)



Delete Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sdwan_other_feature_profile(other_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_sdwan_other_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**|  |

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

# **delete_sdwan_service_feature_profile**
> delete_sdwan_service_feature_profile(service_id)



Delete Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sdwan_service_feature_profile(service_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_sdwan_service_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  |

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

# **delete_sdwan_system_feature_profile**
> delete_sdwan_system_feature_profile(system_id)



Delete Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sdwan_system_feature_profile(system_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_sdwan_system_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  |

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

# **delete_sdwan_transport_feature_profile**
> delete_sdwan_transport_feature_profile(transport_id)



Delete Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sdwan_transport_feature_profile(transport_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_sdwan_transport_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**|  |

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

# **delete_snmp_profile_parcel_for_system**
> delete_snmp_profile_parcel_for_system(system_id, snmp_id)



Delete a Snmp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    snmp_id = "snmpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_snmp_profile_parcel_for_system(system_id, snmp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_snmp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **snmp_id** | **str**| Profile Parcel ID |

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

# **delete_switchport_profile_parcel_for_service**
> delete_switchport_profile_parcel_for_service(service_id, switchport_id)



Delete a Switchport Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    switchport_id = "switchportId_example" # str | Switchport Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_switchport_profile_parcel_for_service(service_id, switchport_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_switchport_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **switchport_id** | **str**| Switchport Parcel ID |

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

# **delete_thousandeyes_profile_parcel_for_other**
> delete_thousandeyes_profile_parcel_for_other(other_id, thousandeyes_id)



Delete a Thousandeyes Profile Parcel for Other feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile ID
    thousandeyes_id = "thousandeyesId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_thousandeyes_profile_parcel_for_other(other_id, thousandeyes_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_thousandeyes_profile_parcel_for_other: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile ID |
 **thousandeyes_id** | **str**| Profile Parcel ID |

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

# **delete_tracker_profile_parcel_for_transport**
> delete_tracker_profile_parcel_for_transport(transport_id, tracker_id)



Delete a Tracker Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    tracker_id = "trackerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tracker_profile_parcel_for_transport(transport_id, tracker_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_tracker_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **tracker_id** | **str**| Profile Parcel ID |

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

# **delete_wan_vpn_and_routing_bgp_association_for_transport**
> delete_wan_vpn_and_routing_bgp_association_for_transport(transport_id, vpn_id, bgp_id)



Delete a WanVpn parcel and a RoutingBgp Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_and_routing_bgp_association_for_transport(transport_id, vpn_id, bgp_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_and_routing_bgp_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp Parcel ID |

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

# **delete_wan_vpn_interface_cellular_and_tracker_association_for_transport**
> delete_wan_vpn_interface_cellular_and_tracker_association_for_transport(transport_id, vpn_id, cellular_id, tracker_id)



Delete a WanVpnInterfaceCellular and a Tracker Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    cellular_id = "cellularId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_interface_cellular_and_tracker_association_for_transport(transport_id, vpn_id, cellular_id, tracker_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_interface_cellular_and_tracker_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **cellular_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker Parcel ID |

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

# **delete_wan_vpn_interface_cellular_for_transport**
> delete_wan_vpn_interface_cellular_for_transport(transport_id, vpn_id, intf_id)



Delete a wanvpn Cellular interface Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    intf_id = "intfId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_interface_cellular_for_transport(transport_id, vpn_id, intf_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_interface_cellular_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **intf_id** | **str**| Interface Parcel ID |

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

# **delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport**
> delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)



Delete a WanVpnInterfaceEthernet and a Tracker Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_interface_ethernet_and_tracker_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker Parcel ID |

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

# **delete_wan_vpn_interface_ethernet_for_transport**
> delete_wan_vpn_interface_ethernet_for_transport(transport_id, vpn_id, ethernet_id)



Delete a  WanVpn InterfaceEthernet Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_interface_ethernet_for_transport(transport_id, vpn_id, ethernet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_interface_ethernet_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

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

# **delete_wan_vpn_profile_parcel_for_transport**
> delete_wan_vpn_profile_parcel_for_transport(transport_id, vpn_id)



Delete a Wan Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wan_vpn_profile_parcel_for_transport(transport_id, vpn_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wan_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

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

# **delete_wirelesslan_profile_parcel_for_service**
> delete_wirelesslan_profile_parcel_for_service(service_id, wirelesslan_id)



Delete a Wirelesslan Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    wirelesslan_id = "wirelesslanId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_wirelesslan_profile_parcel_for_service(service_id, wirelesslan_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->delete_wirelesslan_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **wirelesslan_id** | **str**| Profile Parcel ID |

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

# **edit_aaa_profile_parcel_for_system**
> str edit_aaa_profile_parcel_for_system(system_id, aaa_id)



Update a Aaa Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    aaa_id = "aaaId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Aaa Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_aaa_profile_parcel_for_system(system_id, aaa_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_aaa_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_aaa_profile_parcel_for_system(system_id, aaa_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_aaa_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **aaa_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Aaa Profile Parcel | [optional]

### Return type

**str**

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

# **edit_banner_profile_parcel_for_system**
> str edit_banner_profile_parcel_for_system(system_id, banner_id)



Update a Banner Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    banner_id = "bannerId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Banner Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_banner_profile_parcel_for_system(system_id, banner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_banner_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_banner_profile_parcel_for_system(system_id, banner_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_banner_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **banner_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Banner Profile Parcel | [optional]

### Return type

**str**

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

# **edit_basic_profile_parcel_for_system**
> str edit_basic_profile_parcel_for_system(system_id, basic_id)



Update a Basic Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    basic_id = "basicId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Basic Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_basic_profile_parcel_for_system(system_id, basic_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_basic_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_basic_profile_parcel_for_system(system_id, basic_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_basic_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **basic_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Basic Profile Parcel | [optional]

### Return type

**str**

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

# **edit_bfd_profile_parcel_for_system**
> str edit_bfd_profile_parcel_for_system(system_id, bfd_id)



Update a Bfd Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    bfd_id = "bfdId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Bfd Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_bfd_profile_parcel_for_system(system_id, bfd_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_bfd_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_bfd_profile_parcel_for_system(system_id, bfd_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_bfd_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **bfd_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Bfd Profile Parcel | [optional]

### Return type

**str**

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

# **edit_cellular_controller_and_cellular_profile_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id, cellular_profile_id)



Update a CellularController parcel and a CellularProfile Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID
    cellular_profile_id = "cellularProfileId_example" # str | Cellular Profile ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Profile Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id, cellular_profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_controller_and_cellular_profile_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_cellular_controller_and_cellular_profile_parcel_association_for_transport(transport_id, cellular_controller_id, cellular_profile_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_controller_and_cellular_profile_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |
 **cellular_profile_id** | **str**| Cellular Profile ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Profile Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_cellular_controller_profile_parcel_for_transport**
> str edit_cellular_controller_profile_parcel_for_transport(transport_id, cellular_controller_id)



Update a Cellular Controller Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Controller Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_cellular_controller_profile_parcel_for_transport(transport_id, cellular_controller_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_controller_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_cellular_controller_profile_parcel_for_transport(transport_id, cellular_controller_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_controller_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Controller Profile Parcel | [optional]

### Return type

**str**

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

# **edit_cellular_profile_profile_parcel_for_transport**
> str edit_cellular_profile_profile_parcel_for_transport(transport_id, cellular_profile_id)



Update a Cellular Profile Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_profile_id = "cellularProfileId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Cellular Profile Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_cellular_profile_profile_parcel_for_transport(transport_id, cellular_profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_profile_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_cellular_profile_profile_parcel_for_transport(transport_id, cellular_profile_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_cellular_profile_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_profile_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Cellular Profile Profile Parcel | [optional]

### Return type

**str**

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

# **edit_config_profile_parcel_for_cli**
> str edit_config_profile_parcel_for_cli(cli_id, config_id)



Update a config Profile Parcel for cli feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile ID
    config_id = "configId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | cli config Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_config_profile_parcel_for_cli(cli_id, config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_config_profile_parcel_for_cli: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_config_profile_parcel_for_cli(cli_id, config_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_config_profile_parcel_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile ID |
 **config_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| cli config Profile Parcel | [optional]

### Return type

**str**

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

# **edit_dhcp_server_profile_parcel_for_service**
> str edit_dhcp_server_profile_parcel_for_service(service_id, dhcp_server_id)



Update a Dhcp Server Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    dhcp_server_id = "dhcpServerId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Dhcp Server Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_dhcp_server_profile_parcel_for_service(service_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_dhcp_server_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_dhcp_server_profile_parcel_for_service(service_id, dhcp_server_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_dhcp_server_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **dhcp_server_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Dhcp Server Profile Parcel | [optional]

### Return type

**str**

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

# **edit_global_profile_parcel_for_system**
> str edit_global_profile_parcel_for_system(system_id, global_id)



Update a Global Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    global_id = "globalId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Global Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_global_profile_parcel_for_system(system_id, global_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_global_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_global_profile_parcel_for_system(system_id, global_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_global_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **global_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Global Profile Parcel | [optional]

### Return type

**str**

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

# **edit_lan_vpn_and_routing_bgp_parcel_association_for_service**
> bool, date, datetime, dict, float, int, list, str, none_type edit_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id, bgp_id)



Update a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_and_routing_bgp_parcel_association_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_and_routing_bgp_parcel_association_for_service(service_id, vpn_id, bgp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_and_routing_bgp_parcel_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_lan_vpn_and_routing_ospf_parcel_association_for_service**
> bool, date, datetime, dict, float, int, list, str, none_type edit_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id, ospf_id)



Update a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ospf_id = "ospfId_example" # str | Routing Ospf ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Ospf Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id, ospf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_and_routing_ospf_parcel_association_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_and_routing_ospf_parcel_association_for_service(service_id, vpn_id, ospf_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_and_routing_ospf_parcel_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ospf_id** | **str**| Routing Ospf ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Ospf Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)



Update a LanVpnInterfaceEthernet parcel and a DhcpServer Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | DhcpServer Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_ethernet_and_dhcp_server_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| DhcpServer Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_lan_vpn_interface_ethernet_parcel_for_service**
> str edit_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id, ethernet_id)



Update a LanVpn InterfaceEthernet Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_ethernet_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_interface_ethernet_parcel_for_service(service_id, vpn_id, ethernet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_ethernet_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)



Update a LanVpnInterfaceSvi parcel and a DhcpServer Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | DhcpServer Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(service_id, vpn_id, svi_id, dhcp_server_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| DhcpServer Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_lan_vpn_interface_svi_parcel_for_service**
> str edit_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id, svi_id)



Update a LanVpn InterfaceSvi Parcel for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Interface Svi Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id, svi_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_svi_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_interface_svi_parcel_for_service(service_id, vpn_id, svi_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_interface_svi_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Interface Svi Profile Parcel | [optional]

### Return type

**str**

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

# **edit_lan_vpn_profile_parcel_for_service**
> str edit_lan_vpn_profile_parcel_for_service(service_id, vpn_id)



Update a Lan Vpn Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Lan Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_lan_vpn_profile_parcel_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_lan_vpn_profile_parcel_for_service(service_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_lan_vpn_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Lan Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **edit_logging_profile_parcel_for_system**
> str edit_logging_profile_parcel_for_system(system_id, logging_id)



Update a Logging Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    logging_id = "loggingId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Logging Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_logging_profile_parcel_for_system(system_id, logging_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_logging_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_logging_profile_parcel_for_system(system_id, logging_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_logging_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **logging_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Logging Profile Parcel | [optional]

### Return type

**str**

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

# **edit_management_vpn_interface_ethernet_parcel_for_transport**
> str edit_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id)



Update a ManagementVpn InterfaceEthernet Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Management Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_management_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_management_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_management_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Management Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **edit_management_vpn_profile_parcel_for_transport**
> str edit_management_vpn_profile_parcel_for_transport(transport_id, vpn_id)



Update a Management Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Management Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_management_vpn_profile_parcel_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_management_vpn_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_management_vpn_profile_parcel_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_management_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Management Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **edit_ntp_profile_parcel_for_system**
> str edit_ntp_profile_parcel_for_system(system_id, ntp_id)



Update a Ntp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    ntp_id = "ntpId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Ntp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_ntp_profile_parcel_for_system(system_id, ntp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_ntp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_ntp_profile_parcel_for_system(system_id, ntp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_ntp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **ntp_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Ntp Profile Parcel | [optional]

### Return type

**str**

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

# **edit_omp_profile_parcel_for_system**
> str edit_omp_profile_parcel_for_system(system_id, omp_id)



Update a Omp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    omp_id = "ompId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Omp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_omp_profile_parcel_for_system(system_id, omp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_omp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_omp_profile_parcel_for_system(system_id, omp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_omp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **omp_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Omp Profile Parcel | [optional]

### Return type

**str**

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

# **edit_routing_bgp_profile_parcel_for_service**
> str edit_routing_bgp_profile_parcel_for_service(service_id, bgp_id)



Update a Routing Bgp Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_routing_bgp_profile_parcel_for_service(service_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_bgp_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_routing_bgp_profile_parcel_for_service(service_id, bgp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_bgp_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**str**

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

# **edit_routing_bgp_profile_parcel_for_transport**
> str edit_routing_bgp_profile_parcel_for_transport(transport_id, bgp_id)



Update a Routing Bgp Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_routing_bgp_profile_parcel_for_transport(transport_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_bgp_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_routing_bgp_profile_parcel_for_transport(transport_id, bgp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_bgp_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**str**

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

# **edit_routing_ospf_profile_parcel_for_service**
> str edit_routing_ospf_profile_parcel_for_service(service_id, ospf_id)



Update a Routing Ospf Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    ospf_id = "ospfId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Ospf Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_routing_ospf_profile_parcel_for_service(service_id, ospf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_ospf_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_routing_ospf_profile_parcel_for_service(service_id, ospf_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_routing_ospf_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **ospf_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Ospf Profile Parcel | [optional]

### Return type

**str**

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

# **edit_sdwan_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type edit_sdwan_feature_profile(cli_id)



Edit a SDWAN Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile Id
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_sdwan_feature_profile(cli_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_feature_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_sdwan_feature_profile(cli_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile Id |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_sdwan_other_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type edit_sdwan_other_feature_profile(other_id)



Edit a SDWAN Other Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile Id
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_sdwan_other_feature_profile(other_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_other_feature_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_sdwan_other_feature_profile(other_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_other_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile Id |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_sdwan_service_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type edit_sdwan_service_feature_profile(service_id)



Edit a SDWAN Service Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile Id
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_sdwan_service_feature_profile(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_service_feature_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_sdwan_service_feature_profile(service_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_service_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile Id |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_sdwan_system_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type edit_sdwan_system_feature_profile(system_id)



Edit a SDWAN System Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile Id
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_sdwan_system_feature_profile(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_system_feature_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_sdwan_system_feature_profile(system_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_system_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile Id |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_sdwan_transport_feature_profile**
> bool, date, datetime, dict, float, int, list, str, none_type edit_sdwan_transport_feature_profile(transport_id)



Edit a SDWAN Transport Feature Profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile Id
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | SDWAN Feature profile (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_sdwan_transport_feature_profile(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_transport_feature_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_sdwan_transport_feature_profile(transport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_sdwan_transport_feature_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile Id |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDWAN Feature profile | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_snmp_profile_parcel_for_system**
> str edit_snmp_profile_parcel_for_system(system_id, snmp_id)



Update a Snmp Profile Parcel for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    snmp_id = "snmpId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Snmp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_snmp_profile_parcel_for_system(system_id, snmp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_snmp_profile_parcel_for_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_snmp_profile_parcel_for_system(system_id, snmp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_snmp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **snmp_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Snmp Profile Parcel | [optional]

### Return type

**str**

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

# **edit_switchport_parcel_association_for_service**
> str edit_switchport_parcel_association_for_service(service_id, switchport_id)



Update a Switchport Parcel association for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    switchport_id = "switchportId_example" # str | Switchport ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Switchport Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_switchport_parcel_association_for_service(service_id, switchport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_switchport_parcel_association_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_switchport_parcel_association_for_service(service_id, switchport_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_switchport_parcel_association_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **switchport_id** | **str**| Switchport ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Switchport Profile Parcel | [optional]

### Return type

**str**

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

# **edit_thousandeyes_profile_parcel_for_other**
> str edit_thousandeyes_profile_parcel_for_other(other_id, thousandeyes_id)



Update a Thousandeyes Profile Parcel for Other feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile ID
    thousandeyes_id = "thousandeyesId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Thousandeyes Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_thousandeyes_profile_parcel_for_other(other_id, thousandeyes_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_thousandeyes_profile_parcel_for_other: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_thousandeyes_profile_parcel_for_other(other_id, thousandeyes_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_thousandeyes_profile_parcel_for_other: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile ID |
 **thousandeyes_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Thousandeyes Profile Parcel | [optional]

### Return type

**str**

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

# **edit_tracker_profile_parcel_for_transport**
> str edit_tracker_profile_parcel_for_transport(transport_id, tracker_id)



Update a Tracker Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    tracker_id = "trackerId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_tracker_profile_parcel_for_transport(transport_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_tracker_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_tracker_profile_parcel_for_transport(transport_id, tracker_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_tracker_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **tracker_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel | [optional]

### Return type

**str**

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

# **edit_wan_vpn_and_routing_bgp_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id, bgp_id)



Update a WanVpn parcel and a RoutingBgp Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Routing Bgp Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_and_routing_bgp_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_and_routing_bgp_parcel_association_for_transport(transport_id, vpn_id, bgp_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_and_routing_bgp_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Routing Bgp Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_id, cellular_id, tracker_id)



Update a WanVpnInterfaceCellular parcel and a Tracker Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    cellular_id = "cellularId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_id, cellular_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport(transport_id, vpn_id, cellular_id, tracker_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_cellular_and_tracker_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **cellular_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_wan_vpn_interface_cellular_parcel_for_transport**
> str edit_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id, intf_id)



Update a wanvpn Cellular Interface Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    intf_id = "intfId_example" # str | Interface ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | WanVpn Cellular Interface Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id, intf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_cellular_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_interface_cellular_parcel_for_transport(transport_id, vpn_id, intf_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_cellular_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **intf_id** | **str**| Interface ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| WanVpn Cellular Interface Profile Parcel | [optional]

### Return type

**str**

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

# **edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport**
> bool, date, datetime, dict, float, int, list, str, none_type edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)



Update a WanVpnInterfaceEthernet parcel and a Tracker Parcel association for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Tracker Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(transport_id, vpn_id, ethernet_id, tracker_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Tracker Profile Parcel | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **edit_wan_vpn_interface_ethernet_parcel_for_transport**
> str edit_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id)



Update a WanVpn InterfaceEthernet Parcel for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wan Vpn Interface Ethernet Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_interface_ethernet_parcel_for_transport(transport_id, vpn_id, ethernet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_interface_ethernet_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wan Vpn Interface Ethernet Profile Parcel | [optional]

### Return type

**str**

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

# **edit_wan_vpn_profile_parcel_for_transport**
> str edit_wan_vpn_profile_parcel_for_transport(transport_id, vpn_id)



Update a Wan Vpn Profile Parcel for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wan Vpn Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wan_vpn_profile_parcel_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_profile_parcel_for_transport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wan_vpn_profile_parcel_for_transport(transport_id, vpn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wan_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wan Vpn Profile Parcel | [optional]

### Return type

**str**

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

# **edit_wirelesslan_profile_parcel_for_service**
> str edit_wirelesslan_profile_parcel_for_service(service_id, wirelesslan_id)



Update a Wirelesslan Profile Parcel for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    wirelesslan_id = "wirelesslanId_example" # str | Profile Parcel ID
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | Wirelesslan Profile Parcel (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_wirelesslan_profile_parcel_for_service(service_id, wirelesslan_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wirelesslan_profile_parcel_for_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_wirelesslan_profile_parcel_for_service(service_id, wirelesslan_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->edit_wirelesslan_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **wirelesslan_id** | **str**| Profile Parcel ID |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| Wirelesslan Profile Parcel | [optional]

### Return type

**str**

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

# **get_aaa_profile_parcel_by_parcel_id_for_system**
> str get_aaa_profile_parcel_by_parcel_id_for_system(system_id, aaa_id)



Get Aaa Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    aaa_id = "aaaId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aaa_profile_parcel_by_parcel_id_for_system(system_id, aaa_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_aaa_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **aaa_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_aaa_profile_parcel_for_system**
> str get_aaa_profile_parcel_for_system(system_id)



Get Aaa Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aaa_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_aaa_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_banner_profile_parcel_by_parcel_id_for_system**
> str get_banner_profile_parcel_by_parcel_id_for_system(system_id, banner_id)



Get Banner Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    banner_id = "bannerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_banner_profile_parcel_by_parcel_id_for_system(system_id, banner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_banner_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **banner_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_banner_profile_parcel_for_system**
> str get_banner_profile_parcel_for_system(system_id)



Get Banner Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_banner_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_banner_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_basic_profile_parcel_by_parcel_id_for_system**
> str get_basic_profile_parcel_by_parcel_id_for_system(system_id, basic_id)



Get Basic Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    basic_id = "basicId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_basic_profile_parcel_by_parcel_id_for_system(system_id, basic_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_basic_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **basic_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_basic_profile_parcel_for_system**
> str get_basic_profile_parcel_for_system(system_id)



Get Basic Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_basic_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_basic_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_bfd_profile_parcel_by_parcel_id_for_system**
> str get_bfd_profile_parcel_by_parcel_id_for_system(system_id, bfd_id)



Get Bfd Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    bfd_id = "bfdId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bfd_profile_parcel_by_parcel_id_for_system(system_id, bfd_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_bfd_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **bfd_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_bfd_profile_parcel_for_system**
> str get_bfd_profile_parcel_for_system(system_id)



Get Bfd Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bfd_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_bfd_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema**
> str get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema(schema_type)



Get a Cedge Service LanVpn InterfaceSvi Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cedge_service_lan_vpn_interface_svi_parcel_schema_by_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_cedge_service_switchport_parcel_schema_by_schema_type**
> str get_cedge_service_switchport_parcel_schema_by_schema_type(schema_type)



Get a Cedge Service Switchport Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cedge_service_switchport_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cedge_service_switchport_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_cedge_system_global_parcel_schema_by_schema_type**
> str get_cedge_system_global_parcel_schema_by_schema_type(schema_type)



Get a Cedge System Global Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cedge_system_global_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cedge_system_global_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport**
> str get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_controller_id, cellular_profile_id)



Get CellularController parcel associated CellularProfile Parcel by cellularProfileId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID
    cellular_profile_id = "cellularProfileId_example" # str | Cellular Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_controller_id, cellular_profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |
 **cellular_profile_id** | **str**| Cellular Profile Parcel ID |

### Return type

**str**

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

# **get_cellular_controller_associated_cellular_profile_parcels_for_transport**
> str get_cellular_controller_associated_cellular_profile_parcels_for_transport(transport_id, cellular_controller_id)



Get CellularController associated Cellular Profile Parcels for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_controller_associated_cellular_profile_parcels_for_transport(transport_id, cellular_controller_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_controller_associated_cellular_profile_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_cellular_controller_profile_parcel_by_parcel_id_for_transport**
> str get_cellular_controller_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_controller_id)



Get Cellular Controller Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_controller_id = "cellularControllerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_controller_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_controller_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_controller_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_controller_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_cellular_controller_profile_parcel_for_transport**
> str get_cellular_controller_profile_parcel_for_transport(transport_id)



Get Cellular Controller Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_controller_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_controller_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_cellular_profile_profile_parcel_by_parcel_id_for_transport**
> str get_cellular_profile_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_profile_id)



Get Cellular Profile Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    cellular_profile_id = "cellularProfileId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_profile_profile_parcel_by_parcel_id_for_transport(transport_id, cellular_profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_profile_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **cellular_profile_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_cellular_profile_profile_parcel_for_transport**
> str get_cellular_profile_profile_parcel_for_transport(transport_id)



Get Cellular Profile Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cellular_profile_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_cellular_profile_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_config_profile_parcel_by_parcel_id_for_cli**
> str get_config_profile_parcel_by_parcel_id_for_cli(cli_id, config_id)



Get config Profile Parcel by configId for cli feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile ID
    config_id = "configId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_config_profile_parcel_by_parcel_id_for_cli(cli_id, config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_config_profile_parcel_by_parcel_id_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile ID |
 **config_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_config_profile_parcel_for_cli**
> str get_config_profile_parcel_for_cli(cli_id)



Get config Profile Parcels for cli feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_config_profile_parcel_for_cli(cli_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_config_profile_parcel_for_cli: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_dhcp_server_profile_parcel_by_parcel_id_for_service**
> str get_dhcp_server_profile_parcel_by_parcel_id_for_service(service_id, dhcp_server_id)



Get Dhcp Server Profile Parcel by parcelId for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    dhcp_server_id = "dhcpServerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dhcp_server_profile_parcel_by_parcel_id_for_service(service_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_dhcp_server_profile_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **dhcp_server_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_dhcp_server_profile_parcel_for_service**
> str get_dhcp_server_profile_parcel_for_service(service_id)



Get Dhcp Server Profile Parcels for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dhcp_server_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_dhcp_server_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_global_profile_parcel_by_parcel_id_for_system**
> str get_global_profile_parcel_by_parcel_id_for_system(system_id, global_id)



Get Global Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    global_id = "globalId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_global_profile_parcel_by_parcel_id_for_system(system_id, global_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_global_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **global_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_global_profile_parcel_for_system**
> str get_global_profile_parcel_for_system(system_id)



Get Global Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_global_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_global_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_interface_cellular_parcels_for_transport_wan_vpn**
> str get_interface_cellular_parcels_for_transport_wan_vpn(transport_id, vpn_id)



Get Interface Cellular Parcels for transport Wan Vpn Parcel

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface_cellular_parcels_for_transport_wan_vpn(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_interface_cellular_parcels_for_transport_wan_vpn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_interface_ethernet_parcels_for_service_lan_vpn**
> str get_interface_ethernet_parcels_for_service_lan_vpn(service_id, vpn_id)



Get InterfaceEthernet Parcels for service LanVpn Parcel

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface_ethernet_parcels_for_service_lan_vpn(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_interface_ethernet_parcels_for_service_lan_vpn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_interface_ethernet_parcels_for_transport_management_vpn**
> str get_interface_ethernet_parcels_for_transport_management_vpn(transport_id, vpn_id)



Get InterfaceEthernet Parcels for transport ManagementVpn Parcel

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface_ethernet_parcels_for_transport_management_vpn(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_interface_ethernet_parcels_for_transport_management_vpn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_interface_ethernet_parcels_for_transport_wan_vpn**
> str get_interface_ethernet_parcels_for_transport_wan_vpn(transport_id, vpn_id)



Get InterfaceEthernet Parcels for transport WanVpn Parcel

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface_ethernet_parcels_for_transport_wan_vpn(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_interface_ethernet_parcels_for_transport_wan_vpn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_interface_svi_parcels_for_service_lan_vpn**
> str get_interface_svi_parcels_for_service_lan_vpn(service_id, vpn_id)



Get InterfaceSvi Parcels for service LanVpn Parcel

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface_svi_parcels_for_service_lan_vpn(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_interface_svi_parcels_for_service_lan_vpn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service**
> str get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service(service_id, vpn_id, bgp_id)



Get LanVpn parcel associated RoutingBgp Parcel by bgpId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service(service_id, vpn_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_associated_routing_bgp_parcels_for_service**
> str get_lan_vpn_associated_routing_bgp_parcels_for_service(service_id, vpn_id)



Get LanVpn associated Routing Bgp Parcels for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_associated_routing_bgp_parcels_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_associated_routing_bgp_parcels_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service**
> str get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service(service_id, vpn_id, ospf_id)



Get LanVpn parcel associated RoutingOspf Parcel by ospfId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ospf_id = "ospfId_example" # str | Routing Ospf Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service(service_id, vpn_id, ospf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ospf_id** | **str**| Routing Ospf Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_associated_routing_ospf_parcels_for_service**
> str get_lan_vpn_associated_routing_ospf_parcels_for_service(service_id, vpn_id)



Get LanVpn associated Routing Ospf Parcels for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_associated_routing_ospf_parcels_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_associated_routing_ospf_parcels_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport**
> str get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)



Get LanVpnInterfaceEthernet associated DhcpServer Parcel by dhcpServerId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport(service_id, vpn_id, ethernet_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_ethernet_associated_dhcp_server_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport**
> str get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport(service_id, vpn_id, ethernet_id)



Get LanVpnInterfaceEthernet associated DhcpServer Parcels for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport(service_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_ethernet_associated_dhcp_server_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service**
> str get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service(service_id, vpn_id, ethernet_id)



Get LanVpn InterfaceEthernet Parcel by ethernetId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service(service_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport**
> str get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)



Get LanVpnInterfaceSvi associated DhcpServer Parcel by dhcpServerId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Profile Parcel ID
    dhcp_server_id = "dhcpServerId_example" # str | DhcpServer Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport(service_id, vpn_id, svi_id, dhcp_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface Profile Parcel ID |
 **dhcp_server_id** | **str**| DhcpServer Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport**
> str get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport(service_id, vpn_id, svi_id)



Get LanVpnInterfaceSvi associated DhcpServer Parcels for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID
    svi_id = "sviId_example" # str | Interface Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport(service_id, vpn_id, svi_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |
 **svi_id** | **str**| Interface Profile Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service**
> str get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service(service_id, vpn_id, svi_id)



Get LanVpn InterfaceSvi Parcel by sviId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    svi_id = "sviId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service(service_id, vpn_id, svi_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **svi_id** | **str**| Interface Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_profile_parcel_by_parcel_id_for_service**
> str get_lan_vpn_profile_parcel_by_parcel_id_for_service(service_id, vpn_id)



Get Lan Vpn Profile Parcel by parcelId for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_profile_parcel_by_parcel_id_for_service(service_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_profile_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_lan_vpn_profile_parcel_for_service**
> str get_lan_vpn_profile_parcel_for_service(service_id)



Get Lan Vpn Profile Parcels for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lan_vpn_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_lan_vpn_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_logging_profile_parcel_by_parcel_id_for_system**
> str get_logging_profile_parcel_by_parcel_id_for_system(system_id, logging_id)



Get Logging Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    logging_id = "loggingId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_logging_profile_parcel_by_parcel_id_for_system(system_id, logging_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_logging_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **logging_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_logging_profile_parcel_for_system**
> str get_logging_profile_parcel_for_system(system_id)



Get Logging Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_logging_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_logging_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport**
> str get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id)



Get ManagementVpn InterfaceEthernet Parcel by ethernetId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

### Return type

**str**

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

# **get_management_vpn_profile_parcel_by_parcel_id_for_transport**
> str get_management_vpn_profile_parcel_by_parcel_id_for_transport(transport_id, vpn_id)



Get Management Vpn Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_management_vpn_profile_parcel_by_parcel_id_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_management_vpn_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_management_vpn_profile_parcel_for_transport**
> str get_management_vpn_profile_parcel_for_transport(transport_id)



Get Management Vpn Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_management_vpn_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_management_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_ntp_profile_parcel_by_parcel_id_for_system**
> str get_ntp_profile_parcel_by_parcel_id_for_system(system_id, ntp_id)



Get Ntp Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    ntp_id = "ntpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ntp_profile_parcel_by_parcel_id_for_system(system_id, ntp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_ntp_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **ntp_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_ntp_profile_parcel_for_system**
> str get_ntp_profile_parcel_for_system(system_id)



Get Ntp Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ntp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_ntp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_omp_profile_parcel_by_parcel_id_for_system**
> str get_omp_profile_parcel_by_parcel_id_for_system(system_id, omp_id)



Get Omp Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    omp_id = "ompId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_omp_profile_parcel_by_parcel_id_for_system(system_id, omp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_omp_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **omp_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_omp_profile_parcel_for_system**
> str get_omp_profile_parcel_for_system(system_id)



Get Omp Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_omp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_omp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_routing_bgp_profile_parcel_by_parcel_id_for_service**
> str get_routing_bgp_profile_parcel_by_parcel_id_for_service(service_id, bgp_id)



Get Routing Bgp Profile Parcel by parcelId for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_bgp_profile_parcel_by_parcel_id_for_service(service_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_bgp_profile_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_routing_bgp_profile_parcel_by_parcel_id_for_transport**
> str get_routing_bgp_profile_parcel_by_parcel_id_for_transport(transport_id, bgp_id)



Get Routing Bgp Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    bgp_id = "bgpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_bgp_profile_parcel_by_parcel_id_for_transport(transport_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_bgp_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **bgp_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_routing_bgp_profile_parcel_for_service**
> str get_routing_bgp_profile_parcel_for_service(service_id)



Get Routing Bgp Profile Parcels for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_bgp_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_bgp_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_routing_bgp_profile_parcel_for_transport**
> str get_routing_bgp_profile_parcel_for_transport(transport_id)



Get Routing Bgp Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_bgp_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_bgp_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_routing_ospf_profile_parcel_by_parcel_id_for_service**
> str get_routing_ospf_profile_parcel_by_parcel_id_for_service(service_id, ospf_id)



Get Routing Ospf Profile Parcel by parcelId for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    ospf_id = "ospfId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_ospf_profile_parcel_by_parcel_id_for_service(service_id, ospf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_ospf_profile_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **ospf_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_routing_ospf_profile_parcel_for_service**
> str get_routing_ospf_profile_parcel_for_service(service_id)



Get Routing Ospf Profile Parcels for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_routing_ospf_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_routing_ospf_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_sdwan_feature_profile_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_feature_profile_by_profile_id(cli_id)



Get a SDWAN Feature Profile with Cli profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    cli_id = "cliId_example" # str | Feature Profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_feature_profile_by_profile_id(cli_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_feature_profile_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_id** | **str**| Feature Profile Id |

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

# **get_sdwan_feature_profile_by_sdwan_family**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_feature_profile_by_sdwan_family()



Get all SDWAN Feature Profiles

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_feature_profile_by_sdwan_family(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_feature_profile_by_sdwan_family: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_feature_profiles_by_family_and_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_feature_profiles_by_family_and_type()



Get all SDWAN Feature Profiles with giving Family and profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_feature_profiles_by_family_and_type(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_feature_profiles_by_family_and_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_other_feature_profile_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_other_feature_profile_by_profile_id(other_id)



Get a SDWAN Other Feature Profile with otherId

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_other_feature_profile_by_profile_id(other_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_other_feature_profile_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile Id |

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

# **get_sdwan_other_feature_profiles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_other_feature_profiles()



Get all SDWAN Feature Profiles with giving Family and profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_other_feature_profiles(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_other_feature_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_other_thousandeyes_parcel_schema_by_schema_type**
> str get_sdwan_other_thousandeyes_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Other Thousandeyes Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_other_thousandeyes_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_other_thousandeyes_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_dhcp_server_parcel_schema_by_schema_type**
> str get_sdwan_service_dhcp_server_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Service DhcpServer Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_dhcp_server_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_dhcp_server_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_feature_profile_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_service_feature_profile_by_profile_id(service_id)



Get a SDWAN Service Feature Profile with serviceId

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_feature_profile_by_profile_id(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_feature_profile_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile Id |

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

# **get_sdwan_service_feature_profiles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_service_feature_profiles()



Get all SDWAN Feature Profiles with giving Family and profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_service_feature_profiles(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_feature_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema**
> str get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)



Get a SDWAN Service LanVpn InterfaceEthernet Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_lan_vpn_interface_ethernet_parcel_schema_by_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_lan_vpn_parcel_schema_by_schema_type**
> str get_sdwan_service_lan_vpn_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Service LanVpn Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_lan_vpn_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_lan_vpn_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_routing_bgp_parcel_schema_by_schema_type**
> str get_sdwan_service_routing_bgp_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Service RoutingBgp Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_routing_bgp_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_routing_bgp_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_routing_ospf_parcel_schema_by_schema_type**
> str get_sdwan_service_routing_ospf_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Service RoutingOspf Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_routing_ospf_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_routing_ospf_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_service_wirelesslan_parcel_schema_by_schema_type**
> str get_sdwan_service_wirelesslan_parcel_schema_by_schema_type(schema_type)



Get a sdwan Service Wirelesslan Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_service_wirelesslan_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_service_wirelesslan_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_aaa_parcel_schema_by_schema_type**
> str get_sdwan_system_aaa_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Aaa Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_aaa_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_aaa_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_banner_parcel_schema_by_schema_type**
> str get_sdwan_system_banner_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Banner Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_banner_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_banner_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_basic_parcel_schema_by_schema_type**
> str get_sdwan_system_basic_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Basic Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_basic_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_basic_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_bfd_parcel_schema_by_schema_type**
> str get_sdwan_system_bfd_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Bfd Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_bfd_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_bfd_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_feature_profile_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_system_feature_profile_by_profile_id(system_id)



Get a SDWAN System Feature Profile with systemId

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_feature_profile_by_profile_id(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_feature_profile_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile Id |

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

# **get_sdwan_system_feature_profiles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_system_feature_profiles()



Get all SDWAN Feature Profiles with giving Family and profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_system_feature_profiles(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_feature_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_system_logging_parcel_schema_by_schema_type**
> str get_sdwan_system_logging_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Logging Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_logging_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_logging_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_ntp_parcel_schema_by_schema_type**
> str get_sdwan_system_ntp_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Ntp Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_ntp_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_ntp_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_omp_parcel_schema_by_schema_type**
> str get_sdwan_system_omp_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Omp Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_omp_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_omp_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_system_snmp_parcel_schema_by_schema_type**
> str get_sdwan_system_snmp_parcel_schema_by_schema_type(schema_type)



Get a SDWAN System Snmp Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_system_snmp_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_system_snmp_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type**
> str get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport CellularController Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_cellular_controller_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type**
> str get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport CellularProfile Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_cellular_profile_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_feature_profile_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_transport_feature_profile_by_profile_id(transport_id)



Get a SDWAN Transport Feature Profile with transportId

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_feature_profile_by_profile_id(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_feature_profile_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile Id |

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

# **get_sdwan_transport_feature_profiles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sdwan_transport_feature_profiles()



Get all SDWAN Feature Profiles with giving Family and profile type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sdwan_transport_feature_profiles(offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_feature_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit | [optional] if omitted the server will use the default value of 0

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

# **get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema**
> str get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)



Get a SDWAN Transport ManagementVpn InterfaceEthernet Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_management_vpn_interface_ethernet_parcel_schema_by_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_management_vpn_parcel_schema_by_schema_type**
> str get_sdwan_transport_management_vpn_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport ManagementVpn Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_management_vpn_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_management_vpn_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type**
> str get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport RoutingBgp Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_routing_bgp_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_tracker_parcel_schema_by_schema_type**
> str get_sdwan_transport_tracker_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport Tracker Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_tracker_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_tracker_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema**
> str get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema(schema_type)



Get a SDWAN Transport WanVpn CellularInterface Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_wan_vpn_cellular_interface_parcel_schema_by_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema**
> str get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)



Get a SDWAN Transport WanVpn InterfaceEthernet Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_wan_vpn_interface_ethernet_parcel_schema_by_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type**
> str get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type(schema_type)



Get a SDWAN Transport WanVpn Parcel Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    schema_type = "post" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type(schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_sdwan_transport_wan_vpn_parcel_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  |

### Return type

**str**

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

# **get_snmp_profile_parcel_by_parcel_id_for_system**
> str get_snmp_profile_parcel_by_parcel_id_for_system(system_id, snmp_id)



Get Snmp Profile Parcel by parcelId for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID
    snmp_id = "snmpId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_snmp_profile_parcel_by_parcel_id_for_system(system_id, snmp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_snmp_profile_parcel_by_parcel_id_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |
 **snmp_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_snmp_profile_parcel_for_system**
> str get_snmp_profile_parcel_for_system(system_id)



Get Snmp Profile Parcels for System feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    system_id = "systemId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_snmp_profile_parcel_for_system(system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_snmp_profile_parcel_for_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_switchport_parcel_by_parcel_id_for_service**
> str get_switchport_parcel_by_parcel_id_for_service(service_id, switchport_id)



Get Switchport Parcel by switchportId for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    switchport_id = "switchportId_example" # str | Switchport Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_switchport_parcel_by_parcel_id_for_service(service_id, switchport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_switchport_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **switchport_id** | **str**| Switchport Parcel ID |

### Return type

**str**

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

# **get_switchport_parcels_for_service**
> str get_switchport_parcels_for_service(service_id)



Get Switchport Parcels for service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_switchport_parcels_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_switchport_parcels_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_thousandeyes_profile_parcel_by_parcel_id_for_other**
> str get_thousandeyes_profile_parcel_by_parcel_id_for_other(other_id, thousandeyes_id)



Get Thousandeyes Profile Parcel by parcelId for Other feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile ID
    thousandeyes_id = "thousandeyesId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_thousandeyes_profile_parcel_by_parcel_id_for_other(other_id, thousandeyes_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_thousandeyes_profile_parcel_by_parcel_id_for_other: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile ID |
 **thousandeyes_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_thousandeyes_profile_parcel_for_other**
> str get_thousandeyes_profile_parcel_for_other(other_id)



Get Thousandeyes Profile Parcels for Other feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    other_id = "otherId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_thousandeyes_profile_parcel_for_other(other_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_thousandeyes_profile_parcel_for_other: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_tracker_profile_parcel_by_parcel_id_for_transport**
> str get_tracker_profile_parcel_by_parcel_id_for_transport(transport_id, tracker_id)



Get Tracker Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    tracker_id = "trackerId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tracker_profile_parcel_by_parcel_id_for_transport(transport_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_tracker_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **tracker_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_tracker_profile_parcel_for_transport**
> str get_tracker_profile_parcel_for_transport(transport_id)



Get Tracker Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tracker_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_tracker_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport(transport_id, vpn_id, bgp_id)



Get WanVpn parcel associated RoutingBgp Parcel by bgpId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    bgp_id = "bgpId_example" # str | Routing Bgp Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport(transport_id, vpn_id, bgp_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **bgp_id** | **str**| Routing Bgp Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_associated_routing_bgp_parcels_for_transport**
> str get_wan_vpn_associated_routing_bgp_parcels_for_transport(transport_id, vpn_id)



Get WanVpn associated Routing Bgp Parcels for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_associated_routing_bgp_parcels_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_associated_routing_bgp_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport(transport_id, vpn_id, cellular_id, tracker_id)



Get WanVpnInterfaceCellular associated Tracker Parcel by trackerId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    cellular_id = "cellularId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport(transport_id, vpn_id, cellular_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **cellular_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport**
> str get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport(transport_id, vpn_id, cellular_id)



Get WanVpnInterfaceCellular associated Tracker Parcels for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID
    cellular_id = "cellularId_example" # str | Interface Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport(transport_id, vpn_id, cellular_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_cellular_associated_tracker_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |
 **cellular_id** | **str**| Interface Profile Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport(transport_id, vpn_id, intf_id)



Get wanvpn Cellular interface Parcel by intfId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    intf_id = "intfId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport(transport_id, vpn_id, intf_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **intf_id** | **str**| Interface Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)



Get WanVpnInterfaceEthernet associated Tracker Parcel by trackerId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID
    tracker_id = "trackerId_example" # str | Tracker Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id, tracker_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |
 **tracker_id** | **str**| Tracker Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport**
> str get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport(transport_id, vpn_id, ethernet_id)



Get WanVpnInterfaceEthernet associated Tracker Parcels for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Feature Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport(transport_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_ethernet_associated_tracker_parcels_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Feature Parcel ID |
 **ethernet_id** | **str**| Interface Profile Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id)



Get WanVpn InterfaceEthernet Parcel by ethernetId for transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID
    ethernet_id = "ethernetId_example" # str | Interface Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(transport_id, vpn_id, ethernet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |
 **ethernet_id** | **str**| Interface Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_profile_parcel_by_parcel_id_for_transport**
> str get_wan_vpn_profile_parcel_by_parcel_id_for_transport(transport_id, vpn_id)



Get Wan Vpn Profile Parcel by parcelId for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID
    vpn_id = "vpnId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_profile_parcel_by_parcel_id_for_transport(transport_id, vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_profile_parcel_by_parcel_id_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |
 **vpn_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_wan_vpn_profile_parcel_for_transport**
> str get_wan_vpn_profile_parcel_for_transport(transport_id)



Get Wan Vpn Profile Parcels for Transport feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    transport_id = "transportId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_vpn_profile_parcel_for_transport(transport_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wan_vpn_profile_parcel_for_transport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| Feature Profile ID |

### Return type

**str**

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

# **get_wirelesslan_profile_parcel_by_parcel_id_for_service**
> str get_wirelesslan_profile_parcel_by_parcel_id_for_service(service_id, wirelesslan_id)



Get Wirelesslan Profile Parcel by parcelId for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID
    wirelesslan_id = "wirelesslanId_example" # str | Profile Parcel ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wirelesslan_profile_parcel_by_parcel_id_for_service(service_id, wirelesslan_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wirelesslan_profile_parcel_by_parcel_id_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |
 **wirelesslan_id** | **str**| Profile Parcel ID |

### Return type

**str**

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

# **get_wirelesslan_profile_parcel_for_service**
> str get_wirelesslan_profile_parcel_for_service(service_id)



Get Wirelesslan Profile Parcels for Service feature profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_feature_profile_sdwan_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_feature_profile_sdwan_api.ConfigurationFeatureProfileSDWANApi(api_client)
    service_id = "serviceId_example" # str | Feature Profile ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wirelesslan_profile_parcel_for_service(service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationFeatureProfileSDWANApi->get_wirelesslan_profile_parcel_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Feature Profile ID |

### Return type

**str**

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

