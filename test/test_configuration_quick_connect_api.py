"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_quick_connect_api import ConfigurationQuickConnectApi  # noqa: E501


class TestConfigurationQuickConnectApi(unittest.TestCase):
    """ConfigurationQuickConnectApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationQuickConnectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_submit_day0_config(self):
        """Test case for submit_day0_config

        """
        pass


if __name__ == '__main__':
    unittest.main()