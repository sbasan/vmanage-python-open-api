"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.dhcp_pool import DHCPPool
from openapi_client.model.nat_rule import NATRule
from openapi_client.model.network_protocol_all_of import NetworkProtocolAllOf
from openapi_client.model.profile_parcel import ProfileParcel
from openapi_client.model.variable import Variable
globals()['DHCPPool'] = DHCPPool
globals()['NATRule'] = NATRule
globals()['NetworkProtocolAllOf'] = NetworkProtocolAllOf
globals()['ProfileParcel'] = ProfileParcel
globals()['Variable'] = Variable
from openapi_client.model.network_protocol import NetworkProtocol


class TestNetworkProtocol(unittest.TestCase):
    """NetworkProtocol unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkProtocol(self):
        """Test NetworkProtocol"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkProtocol()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
