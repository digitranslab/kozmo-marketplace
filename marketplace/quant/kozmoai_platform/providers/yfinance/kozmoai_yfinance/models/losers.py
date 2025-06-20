"""Yahoo Finance Top Losers Model."""

# pylint: disable=unused-argument

from typing import Any, Optional

from kozmoai_core.provider.abstract.fetcher import Fetcher
from kozmoai_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from kozmoai_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFLosersQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Losers Query.

    Source: https://finance.yahoo.com/screener/predefined/day_losers
    """

    limit: Optional[int] = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFLosersData(YFPredefinedScreenerData):
    """Yahoo Finance Losers Data."""


class YFLosersFetcher(Fetcher[YFLosersQueryParams, list[YFLosersData]]):
    """Yahoo Finance Losers Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFLosersQueryParams:
        """Transform query params."""
        return YFLosersQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFLosersQueryParams,
        credentials: Optional[dict[str, str]],
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from kozmoai_yfinance.utils.helpers import get_defined_screener

        return await get_defined_screener(name="day_losers", limit=query.limit)

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFLosersData]:
        """Transform data."""
        return [
            YFLosersData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]
