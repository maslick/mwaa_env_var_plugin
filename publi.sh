#!/bin/bash

rm -fr dist
rm -fr build
rm -fr mwaa_env_var_plugin.egg-info

python3 setup.py bdist_wheel
twine upload --repository pypi dist/*
