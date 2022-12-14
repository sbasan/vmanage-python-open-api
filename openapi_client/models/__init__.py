# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.advanced_radio_setting import AdvancedRadioSetting
from openapi_client.model.api_re_key_device import ApiReKeyDevice
from openapi_client.model.api_re_key_device_list import ApiReKeyDeviceList
from openapi_client.model.aws_iam_credentials import AwsIamCredentials
from openapi_client.model.aws_key_credentials import AwsKeyCredentials
from openapi_client.model.azure_credentials import AzureCredentials
from openapi_client.model.banner import Banner
from openapi_client.model.bfd import Bfd
from openapi_client.model.bfd_timer_on_transport_tunnels import BfdTimerOnTransportTunnels
from openapi_client.model.biz_internet_timer import BizInternetTimer
from openapi_client.model.cellular import Cellular
from openapi_client.model.cellular_all_of import CellularAllOf
from openapi_client.model.cellular_profile import CellularProfile
from openapi_client.model.certificate_states import CertificateStates
from openapi_client.model.certificate_validity import CertificateValidity
from openapi_client.model.channel_power_settings import ChannelPowerSettings
from openapi_client.model.config_group import ConfigGroup
from openapi_client.model.connect_to_ntp_server import ConnectToNtpServer
from openapi_client.model.control_status import ControlStatus
from openapi_client.model.corporate_wifi import CorporateWifi
from openapi_client.model.country_region_settings import CountryRegionSettings
from openapi_client.model.create_device_params import CreateDeviceParams
from openapi_client.model.create_tenant_model import CreateTenantModel
from openapi_client.model.dhcp_pool import DHCPPool
from openapi_client.model.data_center import DataCenter
from openapi_client.model.data_center_registration import DataCenterRegistration
from openapi_client.model.delete_tenant_bulk_model import DeleteTenantBulkModel
from openapi_client.model.delete_tenant_model import DeleteTenantModel
from openapi_client.model.device import Device
from openapi_client.model.device_health_details import DeviceHealthDetails
from openapi_client.model.device_ip import DeviceIP
from openapi_client.model.device_model import DeviceModel
from openapi_client.model.device_type import DeviceType
from openapi_client.model.device_uuid import DeviceUuid
from openapi_client.model.devices_health import DevicesHealth
from openapi_client.model.devices_health_overview import DevicesHealthOverview
from openapi_client.model.disaster_recovery_settings import DisasterRecoverySettings
from openapi_client.model.domain_detail import DomainDetail
from openapi_client.model.entity_ownership_info import EntityOwnershipInfo
from openapi_client.model.equinix_credentials import EquinixCredentials
from openapi_client.model.equinix_location_info import EquinixLocationInfo
from openapi_client.model.equinix_ne_info import EquinixNEInfo
from openapi_client.model.equinix_partner_port import EquinixPartnerPort
from openapi_client.model.ethernet import Ethernet
from openapi_client.model.ethernet_all_of import EthernetAllOf
from openapi_client.model.ethernet_interface import EthernetInterface
from openapi_client.model.event_name import EventName
from openapi_client.model.feature_profile import FeatureProfile
from openapi_client.model.gcp_credentials import GcpCredentials
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request_value import GetO365PreferredPathFromVAnalyticsRequestValue
from openapi_client.model.global_settings import GlobalSettings
from openapi_client.model.global_settings_all_of import GlobalSettingsAllOf
from openapi_client.model.group_id import GroupId
from openapi_client.model.guest_wifi import GuestWifi
from openapi_client.model.header import Header
from openapi_client.model.header_element import HeaderElement
from openapi_client.model.host import Host
from openapi_client.model.ike_phase import IkePhase
from openapi_client.model.ip_sec_policy import IpSecPolicy
from openapi_client.model.ip_sec_security import IpSecSecurity
from openapi_client.model.logging_system_messages import LoggingSystemMessages
from openapi_client.model.login_access_to_router import LoginAccessToRouter
from openapi_client.model.lte_timer import LteTimer
from openapi_client.model.megaport_credentials import MegaportCredentials
from openapi_client.model.megaport_location_info import MegaportLocationInfo
from openapi_client.model.megaport_mve_info import MegaportMVEInfo
from openapi_client.model.megaport_partner_port import MegaportPartnerPort
from openapi_client.model.mpls_timer import MplsTimer
from openapi_client.model.multi_cloud_account_info import MultiCloudAccountInfo
from openapi_client.model.multi_cloud_edge_account_info import MultiCloudEdgeAccountInfo
from openapi_client.model.multi_cloud_edge_billing_account_info import MultiCloudEdgeBillingAccountInfo
from openapi_client.model.multi_cloud_edge_location_info import MultiCloudEdgeLocationInfo
from openapi_client.model.multi_cloud_edge_partner_port import MultiCloudEdgePartnerPort
from openapi_client.model.nat_rule import NATRule
from openapi_client.model.name_value_pair import NameValuePair
from openapi_client.model.network_protocol import NetworkProtocol
from openapi_client.model.network_protocol_all_of import NetworkProtocolAllOf
from openapi_client.model.node import Node
from openapi_client.model.nwpi_domain_monitor import NwpiDomainMonitor
from openapi_client.model.omp import OMP
from openapi_client.model.on_demand_queue_entry import OnDemandQueueEntry
from openapi_client.model.partner_type import PartnerType
from openapi_client.model.policy_rule import PolicyRule
from openapi_client.model.profile_parcel import ProfileParcel
from openapi_client.model.property_definition import PropertyDefinition
from openapi_client.model.public_internet_timer import PublicInternetTimer
from openapi_client.model.queue_entries import QueueEntries
from openapi_client.model.queue_properties import QueueProperties
from openapi_client.model.radio_band_setting24_g import RadioBandSetting24G
from openapi_client.model.radio_band_setting5_g import RadioBandSetting5G
from openapi_client.model.radius_server import RadiusServer
from openapi_client.model.resource_group import ResourceGroup
from openapi_client.model.ssid_config import SSIDConfig
from openapi_client.model.schema_definition import SchemaDefinition
from openapi_client.model.security_policy import SecurityPolicy
from openapi_client.model.security_policy_all_of import SecurityPolicyAllOf
from openapi_client.model.sim_slot_config import SimSlotConfig
from openapi_client.model.site_health import SiteHealth
from openapi_client.model.site_to_site_vpn import SiteToSiteVpn
from openapi_client.model.smart_account_model import SmartAccountModel
from openapi_client.model.software_upload_file_data import SoftwareUploadFileData
from openapi_client.model.statistics_processing_counters import StatisticsProcessingCounters
from openapi_client.model.stats_type_processing_counters import StatsTypeProcessingCounters
from openapi_client.model.systems import Systems
from openapi_client.model.tag_restful_resource import TagRestfulResource
from openapi_client.model.tenant_status import TenantStatus
from openapi_client.model.tenant_status_list_model import TenantStatusListModel
from openapi_client.model.thread_pool_definition import ThreadPoolDefinition
from openapi_client.model.thread_pools_definition import ThreadPoolsDefinition
from openapi_client.model.update_tenant_model import UpdateTenantModel
from openapi_client.model.update_tenantv_smart_model import UpdateTenantvSmartModel
from openapi_client.model.uuid import Uuid
from openapi_client.model.uuid_to_domain_id import UuidToDomainId
from openapi_client.model.uuid_to_domain_id_mapping import UuidToDomainIdMapping
from openapi_client.model.v_edge_bootstrap_config import VEdgeBootstrapConfig
from openapi_client.model.v_edge_health import VEdgeHealth
from openapi_client.model.vpnid import VPNID
from openapi_client.model.v_resource_group_name_model import VResourceGroupNameModel
from openapi_client.model.v_smart_status import VSmartStatus
from openapi_client.model.variable import Variable
from openapi_client.model.vertex_definition import VertexDefinition
from openapi_client.model.vpn import Vpn
from openapi_client.model.vpn_all_of import VpnAllOf
from openapi_client.model.wan_spec import WanSpec
from openapi_client.model.wifi import Wifi
from openapi_client.model.wifi_all_of import WifiAllOf
