# KozmoAI Tradier Provider

This extension integrates the [Tradier](https://tradier.com) data provider into the KozmoAI Platform.

## Installation

To install the extension:

```bash
pip install kozmoai-tradier
```

Documentation available [here](https://docs.kozmoai.co/platform/developer_guide/contributing).

## Authorization

This extension requires two authorization fields:

- 'tradier_api_key'
- 'tradier_account_type'

Where the account type is either "sandbox" or "live".

Add these to the file, under 'credentials': `~/.kozmoai_platform/user_settings.json`
