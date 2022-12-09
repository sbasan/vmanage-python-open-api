"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.nwpi_api import NWPIApi  # noqa: E501


class TestNWPIApi(unittest.TestCase):
    """NWPIApi unit test stubs"""

    def setUp(self):
        self.api = NWPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_agg_flow(self):
        """Test case for get_agg_flow

        """
        pass

    def test_get_app_qos_data(self):
        """Test case for get_app_qos_data

        """
        pass

    def test_get_app_qos_state(self):
        """Test case for get_app_qos_state

        """
        pass

    def test_get_concurrent_data(self):
        """Test case for get_concurrent_data

        """
        pass

    def test_get_concurrent_domain_data(self):
        """Test case for get_concurrent_domain_data

        """
        pass

    def test_get_event_app_hop_list(self):
        """Test case for get_event_app_hop_list

        """
        pass

    def test_get_event_app_score_bandwidth(self):
        """Test case for get_event_app_score_bandwidth

        """
        pass

    def test_get_event_flow_from_app_hop(self):
        """Test case for get_event_flow_from_app_hop

        """
        pass

    def test_get_event_readout(self):
        """Test case for get_event_readout

        """
        pass

    def test_get_routing_detail_from_local(self):
        """Test case for get_routing_detail_from_local

        """
        pass


if __name__ == '__main__':
    unittest.main()
