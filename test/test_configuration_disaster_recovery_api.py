"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_disaster_recovery_api import ConfigurationDisasterRecoveryApi  # noqa: E501


class TestConfigurationDisasterRecoveryApi(unittest.TestCase):
    """ConfigurationDisasterRecoveryApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationDisasterRecoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate(self):
        """Test case for activate

        """
        pass

    def test_delete(self):
        """Test case for delete

        """
        pass

    def test_delete_dc(self):
        """Test case for delete_dc

        """
        pass

    def test_delete_local_dc(self):
        """Test case for delete_local_dc

        """
        pass

    def test_disaster_recovery_pause_replication(self):
        """Test case for disaster_recovery_pause_replication

        """
        pass

    def test_disaster_recovery_replication_request(self):
        """Test case for disaster_recovery_replication_request

        """
        pass

    def test_disaster_recovery_un_pause_replication(self):
        """Test case for disaster_recovery_un_pause_replication

        """
        pass

    def test_download(self):
        """Test case for download

        """
        pass

    def test_download_replication_data(self):
        """Test case for download_replication_data

        """
        pass

    def test_get(self):
        """Test case for get

        """
        pass

    def test_get_cluster_info(self):
        """Test case for get_cluster_info

        """
        pass

    def test_get_config_db_restore_status(self):
        """Test case for get_config_db_restore_status

        """
        pass

    def test_get_details(self):
        """Test case for get_details

        """
        pass

    def test_get_disaster_recovery_local_replication_schedule(self):
        """Test case for get_disaster_recovery_local_replication_schedule

        """
        pass

    def test_get_disaster_recovery_status(self):
        """Test case for get_disaster_recovery_status

        """
        pass

    def test_get_history(self):
        """Test case for get_history

        """
        pass

    def test_get_local_data_center_state(self):
        """Test case for get_local_data_center_state

        """
        pass

    def test_get_local_history(self):
        """Test case for get_local_history

        """
        pass

    def test_get_reachability_info(self):
        """Test case for get_reachability_info

        """
        pass

    def test_get_remote_data_center_state(self):
        """Test case for get_remote_data_center_state

        """
        pass

    def test_get_remote_data_center_version(self):
        """Test case for get_remote_data_center_version

        """
        pass

    def test_get_remote_dc_members_state(self):
        """Test case for get_remote_dc_members_state

        """
        pass

    def test_getdr_status(self):
        """Test case for getdr_status

        """
        pass

    def test_pause_dr(self):
        """Test case for pause_dr

        """
        pass

    def test_pause_local_arbitrator(self):
        """Test case for pause_local_arbitrator

        """
        pass

    def test_pause_local_dc_for_dr(self):
        """Test case for pause_local_dc_for_dr

        """
        pass

    def test_pause_local_dc_replication(self):
        """Test case for pause_local_dc_replication

        """
        pass

    def test_register(self):
        """Test case for register

        """
        pass

    def test_restart_data_center(self):
        """Test case for restart_data_center

        """
        pass

    def test_restore_config_db(self):
        """Test case for restore_config_db

        """
        pass

    def test_unpause_dr(self):
        """Test case for unpause_dr

        """
        pass

    def test_unpause_local_arbitrator(self):
        """Test case for unpause_local_arbitrator

        """
        pass

    def test_unpause_local_dc_for_dr(self):
        """Test case for unpause_local_dc_for_dr

        """
        pass

    def test_unpause_local_dc_replication(self):
        """Test case for unpause_local_dc_replication

        """
        pass

    def test_update(self):
        """Test case for update

        """
        pass

    def test_update1(self):
        """Test case for update1

        """
        pass

    def test_update_disaster_recovery_state(self):
        """Test case for update_disaster_recovery_state

        """
        pass

    def test_update_disaster_recovery_state1(self):
        """Test case for update_disaster_recovery_state1

        """
        pass

    def test_update_dr_state(self):
        """Test case for update_dr_state

        """
        pass

    def test_update_replication(self):
        """Test case for update_replication

        """
        pass


if __name__ == '__main__':
    unittest.main()