from setuptools import setup
import pathlib

VERSION = '1.0.1'

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='mwaa-env-var-plugin',
      entry_points={
          "airflow.plugins": [
              "mwaa_env_var_plugin = mwaa_env_var_plugin:MwaaEnvVarPlugin"
          ]
      },
      packages=[
          'mwaa_env_var_plugin'
      ],
      version=VERSION,
      license='MIT',
      platforms=['Linux', 'Windows', 'MacOS'],
      description='Environment variable plugin for MWAA',
      long_description=README,
      long_description_content_type='text/markdown',
      author='Pavel Maslov',
      url='https://github.com/maslick/mwaa_env_var_plugin'
)
