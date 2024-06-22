import unittest
from unittest.mock import patch
import os


class TestMwaaEnvVarPlugin(unittest.TestCase):
    @patch.dict(os.environ, {
        'AIRFLOW__ENV__API_KEY': 'test_api_key',
        'AIRFLOW__ENV__DB_PASSWORD': 'test_db_password'
    }, clear=True)
    def test_set_custom_env_vars(self):
        # Import the plugin inside the test method to ensure the mock is applied
        from mwaa_env_var_plugin import MwaaEnvVarPlugin
        module = MwaaEnvVarPlugin()

        # Check if the new environment variables are set correctly
        self.assertEqual(os.environ.get('API_KEY'), 'test_api_key')
        self.assertEqual(os.environ.get('DB_PASSWORD'), 'test_db_password')

        # Ensure original AIRFLOW__CUSTOM__ variables still exist
        self.assertEqual(os.environ.get('AIRFLOW__ENV__API_KEY'), 'test_api_key')
        self.assertEqual(os.environ.get('AIRFLOW__ENV__DB_PASSWORD'), 'test_db_password')


if __name__ == '__main__':
    unittest.main()
