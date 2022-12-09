"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_dre_api import RealTimeMonitoringDREApi  # noqa: E501


class TestRealTimeMonitoringDREApi(unittest.TestCase):
    """RealTimeMonitoringDREApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringDREApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dre_auto_bypass_stats(self):
        """Test case for get_dre_auto_bypass_stats

        """
        pass

    def test_get_dre_peer_stats(self):
        """Test case for get_dre_peer_stats

        """
        pass

    def test_get_dre_stats(self):
        """Test case for get_dre_stats

        """
        pass

    def test_get_dre_status(self):
        """Test case for get_dre_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
