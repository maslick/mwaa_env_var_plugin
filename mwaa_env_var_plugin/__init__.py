import os
from airflow.plugins_manager import AirflowPlugin


class MwaaEnvVarPlugin(AirflowPlugin):
    name = "mwaa_env_var_plugin"

    def __init__(self):
        super().__init__()
        self.set_custom_env_vars()

    def on_load(self, *args, **kwargs):
        print("MwaaEnvVarPlugin loaded.")

    @staticmethod
    def set_custom_env_vars():
        # Iterate over all environment variables
        for env_var, value in os.environ.items():
            # Check if the environment variable starts with AIRFLOW__ENV__
            if env_var.startswith('AIRFLOW__ENV__'):
                # Remove the AIRFLOW__ENV__ prefix and double underscores to create the new variable name
                new_env_var_name = env_var[len('AIRFLOW__ENV__'):]
                # Set the new environment variable
                os.environ[new_env_var_name] = value
                print(f"Setting environment variable: {new_env_var_name}")
