"""Senior Loan Officer Opinion Survey Standard Model."""

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


class SeniorLoanOfficerSurveyQueryParams(QueryParams):
    """Senior Loan Officer Opinion Survey Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class SeniorLoanOfficerSurveyData(Data):
    """Senior Loan Officer Opinion Survey Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    value: float = Field(description="Survey value.")
    title: Optional[str] = Field(description="Survey title.")
