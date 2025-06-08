"""Futures Info Standard Model."""

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class FuturesInfoQueryParams(QueryParams):
    """Futures Info Query."""

    # leaving this empty to let the provider create custom symbol docstrings.


class FuturesInfoData(Data):
    """Futures Instruments Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
