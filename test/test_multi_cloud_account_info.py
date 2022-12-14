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
from openapi_client.model.aws_iam_credentials import AwsIamCredentials
from openapi_client.model.aws_key_credentials import AwsKeyCredentials
from openapi_client.model.azure_credentials import AzureCredentials
from openapi_client.model.gcp_credentials import GcpCredentials
globals()['AwsIamCredentials'] = AwsIamCredentials
globals()['AwsKeyCredentials'] = AwsKeyCredentials
globals()['AzureCredentials'] = AzureCredentials
globals()['GcpCredentials'] = GcpCredentials
from openapi_client.model.multi_cloud_account_info import MultiCloudAccountInfo


class TestMultiCloudAccountInfo(unittest.TestCase):
    """MultiCloudAccountInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMultiCloudAccountInfo(self):
        """Test MultiCloudAccountInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MultiCloudAccountInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
