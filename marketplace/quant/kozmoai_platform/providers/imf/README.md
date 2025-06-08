# KozmoAI IMF Provider Extension

This package adds the `kozmoai-imf` provider extension to the KozmoAI Platform.

## Installation

Install from PyPI with:

```sh
pip install kozmoai-imf
```

## Implementation

The extension utilizes the JSON RESTful Web Service ((https://datahelp.imf.org/knowledgebase/articles/630877-data-services)[https://datahelp.imf.org/knowledgebase/articles/630877-data-services])

No authorization is required to use, but IP addresses are bound by the limitations described in the link above.

## Coverage

- Databases:
  - International Reserves and Foreign Currency Liquidity
  - Direction of Trade Statistics
  - Financial Soundness Indicators

Coverage:
  - All IRFCL tables.
  - Individual, or multiple, time series from single or multiple countries.
  - Core and Encouraged Set tables, plus all individual underlying series.

### Endpoints

- `obb.economy.available_indicators`
- `obb.economy.indicators`
- `obb.economy.direction_of_trade`
