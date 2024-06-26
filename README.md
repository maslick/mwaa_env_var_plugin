# MWAA Environment Variable Plugin

## Overview

The `MwaaEnvVarPlugin` is a custom Apache Airflow plugin designed for Amazon Managed Workflows for Apache Airflow (MWAA). 
This plugin automatically converts [MWAA configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html#configuring-env-variables-customizing) in the `env` section (e.g., `env.foo_bar`) into 
user-friendly environment variables (e.g., `FOO_BAR`), as opposed to the default `AIRFLOW__ENV__FOO_BAR` provided 
by vanilla MWAA.

## Features

- Automatically detects environment variables set by MWAA through configuration variables (`env` section).
- Converts these variables to user-friendly names without the `AIRFLOW__ENV` prefix and double underscores.
- Sets the new environment variables in the system.
- The new variables are available in all processes (Scheduler, Worker, Webserver) and override environment variables that might have been set in `startup.sh` script.

## Installation

1. Simply add `mwaa-env-var-plugin` into your MWAA requirements.txt:

```
mwaa-env-var-plugin==1.0.0
```

2. By default, in Apache Airflow v2, plugins are [configured to be "lazily" loaded](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html#configuring-2.0-airflow-override) using the `core.lazy_load_plugins : True` setting. 
Make sure you add `core.lazy_load_plugins : False` as an Apache Airflow configuration option to load plugins 
at the start of each Airflow process to override the default setting.

## PyPI

https://pypi.org/project/mwaa-env-var-plugin/
