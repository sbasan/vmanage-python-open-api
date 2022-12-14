"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.partner_dnacsdaapi_api import PartnerDNACSDAAPIApi  # noqa: E501


class TestPartnerDNACSDAAPIApi(unittest.TestCase):
    """PartnerDNACSDAAPIApi unit test stubs"""

    def setUp(self):
        self.api = PartnerDNACSDAAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sda_config(self):
        """Test case for create_sda_config

        """
        pass

    def test_create_sda_config_from_netconf(self):
        """Test case for create_sda_config_from_netconf

        """
        pass

    def test_get_device_details(self):
        """Test case for get_device_details

        """
        pass

    def test_get_overlay_vpn_list(self):
        """Test case for get_overlay_vpn_list

        """
        pass

    def test_get_sda_enabled_devices(self):
        """Test case for get_sda_enabled_devices

        """
        pass

    def test_get_sites_for_partner(self):
        """Test case for get_sites_for_partner

        """
        pass


if __name__ == '__main__':
    unittest.main()
