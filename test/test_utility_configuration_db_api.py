"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.utility_configuration_db_api import UtilityConfigurationDBApi  # noqa: E501


class TestUtilityConfigurationDBApi(unittest.TestCase):
    """UtilityConfigurationDBApi unit test stubs"""

    def setUp(self):
        self.api = UtilityConfigurationDBApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_db_size_on_file(self):
        """Test case for get_db_size_on_file

        """
        pass


if __name__ == '__main__':
    unittest.main()