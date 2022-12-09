"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_sig_api import RealTimeMonitoringSIGApi  # noqa: E501


class TestRealTimeMonitoringSIGApi(unittest.TestCase):
    """RealTimeMonitoringSIGApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringSIGApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sig_tunnel_list(self):
        """Test case for get_sig_tunnel_list

        """
        pass

    def test_get_sig_tunnel_total(self):
        """Test case for get_sig_tunnel_total

        """
        pass

    def test_get_sig_umbrella_tunnels(self):
        """Test case for get_sig_umbrella_tunnels

        """
        pass

    def test_get_sig_zscaler_tunnels(self):
        """Test case for get_sig_zscaler_tunnels

        """
        pass

    def test_tunnel_dashboard(self):
        """Test case for tunnel_dashboard

        """
        pass


if __name__ == '__main__':
    unittest.main()