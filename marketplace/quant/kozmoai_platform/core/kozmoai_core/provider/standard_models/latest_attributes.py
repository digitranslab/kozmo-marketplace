"""Latest Attributes Standard Model."""

from typing import List, Optional, Set, Union

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class LatestAttributesQueryParams(QueryParams):
    """Latest Attributes Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))
    tag: str = Field(description="Intrinio data tag ID or code.")

    @field_validator("tag", mode="before", check_fields=False)
    @classmethod
    def multiple_tags(cls, v: Union[str, List[str], Set[str]]):
        """Accept a comma-separated string or list of tags."""
        if isinstance(v, str):
            return v.lower()
        return ",".join([tag.lower() for tag in list(v)])

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class LatestAttributesData(Data):
    """Latest Attributes Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol"))
    tag: Optional[str] = Field(
        default=None, description="Tag name for the fetched data."
    )
    value: Optional[Union[str, float]] = Field(
        default=None, description="The value of the data."
    )
