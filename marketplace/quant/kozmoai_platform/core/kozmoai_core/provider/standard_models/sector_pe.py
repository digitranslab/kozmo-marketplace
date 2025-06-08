"""Sector P/E Ratio Standard Model."""

from datetime import date as dateType
from typing import Optional

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SectorPEQueryParams(QueryParams):
    """Sector P/E Ratio Query."""


class SectorPEData(Data):
    """Sector P/E Ratio Data."""

    date: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("date", ""), default=None
    )
    exchange: Optional[str] = Field(
        default=None, description="The exchange where the data is from."
    )
    sector: str = Field(description="The name of the sector.")
    pe: float = Field(description="The P/E ratio of the sector.")
