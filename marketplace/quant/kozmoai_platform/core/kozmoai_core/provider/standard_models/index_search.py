"""Index Search Standard Model."""

from kozmoai_core.provider.abstract.data import Data
from kozmoai_core.provider.abstract.query_params import QueryParams
from kozmoai_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSearchQueryParams(QueryParams):
    """Index Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class IndexSearchData(Data):
    """Index Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="Name of the index.")
