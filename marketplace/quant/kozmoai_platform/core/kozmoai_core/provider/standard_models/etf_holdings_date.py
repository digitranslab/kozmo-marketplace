"""ETF Holdings Date Standard Model."""

from datetime import date as dateType

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EtfHoldingsDateQueryParams(QueryParams):
    """ETF Holdings Date Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")


class EtfHoldingsDateData(Data):
    """ETF Holdings Date Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
