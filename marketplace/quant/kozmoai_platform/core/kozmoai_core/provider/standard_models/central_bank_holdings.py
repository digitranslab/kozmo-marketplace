"""Central Bank Holdings Standard Model."""

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


class CentralBankHoldingsQueryParams(QueryParams):
    """Central Bank Holdings Query."""

    date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )


class CentralBankHoldingsData(Data):
    """Central Bank Holdings Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
