"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_sfp_api import RealTimeMonitoringSFPApi  # noqa: E501


class TestRealTimeMonitoringSFPApi(unittest.TestCase):
    """RealTimeMonitoringSFPApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringSFPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_detail(self):
        """Test case for get_detail

        """
        pass

    def test_get_diagnostic(self):
        """Test case for get_diagnostic

        """
        pass

    def test_get_diagnostic_measurement_alarm(self):
        """Test case for get_diagnostic_measurement_alarm

        """
        pass

    def test_get_diagnostic_measurement_value(self):
        """Test case for get_diagnostic_measurement_value

        """
        pass


if __name__ == '__main__':
    unittest.main()