"""Yahoo Finance Asset Performance Active Model."""

# pylint: disable=unused-argument

from typing import Any, Optional

from kozmoai_core.provider.abstract.fetcher import Fetcher
from kozmoai_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from kozmoai_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFActiveQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Most Active Query.

    Source: https://finance.yahoo.com/screener/predefined/most_actives
    """

    limit: Optional[int] = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFActiveData(YFPredefinedScreenerData):
    """Yahoo Finance Most Active Data."""


class YFActiveFetcher(Fetcher[YFActiveQueryParams, list[YFActiveData]]):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFActiveQueryParams:
        """Transform query params."""
        return YFActiveQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFActiveQueryParams,
        credentials: Optional[dict[str, str]],
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from kozmoai_yfinance.utils.helpers import get_defined_screener

        return await get_defined_screener(name="most_actives", limit=query.limit)

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFActiveData]:
        """Transform data."""
        return [
            YFActiveData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketVolume"],
                reverse=query.sort == "desc",
            )
        ]
