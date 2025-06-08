"""Cik Map Standard Model."""

from typing import Optional, Union

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CikMapQueryParams(QueryParams):
    """CikMap Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class CikMapData(Data):
    """CikMap Data."""

    cik: Optional[Union[str, int]] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("cik", "")
    )
