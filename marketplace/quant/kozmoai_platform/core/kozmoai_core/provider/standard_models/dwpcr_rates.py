"""Discount Window Primary Credit Rate Standard Model."""

from datetime import (
    date as dateType,
)
from typing import Optional

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class DiscountWindowPrimaryCreditRateParams(QueryParams):
    """Discount Window Primary Credit Rate Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class DiscountWindowPrimaryCreditRateData(Data):
    """Discount Window Primary Credit Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="Discount Window Primary Credit Rate.")
