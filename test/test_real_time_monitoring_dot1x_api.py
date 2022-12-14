"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_dot1x_api import RealTimeMonitoringDOT1xApi  # noqa: E501


class TestRealTimeMonitoringDOT1xApi(unittest.TestCase):
    """RealTimeMonitoringDOT1xApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringDOT1xApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dot1x_radius(self):
        """Test case for get_dot1x_radius

        """
        pass

    def test_get_wlandot1x_clients(self):
        """Test case for get_wlandot1x_clients

        """
        pass

    def test_get_wlandot1x_interfaces(self):
        """Test case for get_wlandot1x_interfaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
