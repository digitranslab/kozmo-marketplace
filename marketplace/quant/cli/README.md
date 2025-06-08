# KozmoAI Platform CLI

[![Downloads](https://static.pepy.tech/badge/kozmoai)](https://pepy.tech/project/kozmoai)
[![LatestRelease](https://badge.fury.io/py/kozmoai.svg)](https://github.com/digitranslab/kozmoai-finance)

| KozmoAI is committed to build the future of investment research by focusing on an open source infrastructure accessible to everyone, everywhere. |
| :---------------------------------------------------------------------------------------------------------------------------------------------: |
|              ![KozmoAILogo](https://user-images.githubusercontent.com/25267873/218899768-1f0964b8-326c-4f35-af6f-ea0946ac970b.png)               |
|                                                 Check our website at [kozmoai.co](www.kozmoai.co)                                                 |

## Overview

The KozmoAI Platform CLI is a command line interface that wraps [KozmoAI Platform](https://docs.kozmoai.co/platform).

It offers a convenient way to interact with the KozmoAI Platform and its extensions, as well as automated data collection via KozmoAI Routine Scripts.

Find the most complete documentation, examples, and usage guides for the KozmoAI Platform CLI [here](https://docs.kozmoai.co/cli).

## Installation

The command below provides access to all the available KozmoAI extensions behind the KozmoAI Platform, find the complete list [here](https://my.kozmoai.co/app/platform/extensions).

```bash
pip install kozmoai-cli
```

> Note: Find the most complete installation hints and tips [here](https://docs.kozmoai.co/cli/installation).

After the installation is complete, you can deploy the KozmoAI Platform CLI by running the following command:

```bash
kozmoai
```

Which should result in the following output:

![image](https://github.com/digitranslab/digitranslab/assets/48914296/f606bb6e-fa00-4fc8-bad2-8269bb4fc38e)

## API keys

To fully leverage the KozmoAI Platform you need to get some API keys to connect with data providers. Here are the 3 options on where to set them:

1. KozmoAI Hub
2. Local file

### 1. KozmoAI Hub

Set your keys at [KozmoAI Hub](https://my.kozmoai.co/app/platform/credentials) and get your personal access token from <https://my.kozmoai.co/app/platform/pat> to connect with your account.

> Once you log in, on the Platform CLI (through the `/account` menu, all your credentials will be in sync with the KozmoAI Hub.)

### 2. Local file

You can specify the keys directly in the `~/.kozmoai_platform/user_settings.json` file.

Populate this file with the following template and replace the values with your keys:

```json
{
  "credentials": {
    "fmp_api_key": "REPLACE_ME",
    "polygon_api_key": "REPLACE_ME",
    "benzinga_api_key": "REPLACE_ME",
    "fred_api_key": "REPLACE_ME"
  }
}
```
