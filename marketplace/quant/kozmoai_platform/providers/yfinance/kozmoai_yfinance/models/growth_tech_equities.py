"""Yahoo Finance Asset Performance Growth Tech Equities Model."""

# pylint: disable=unused-argument

from typing import Any, Optional

from kozmoai_core.provider.abstract.fetcher import Fetcher
from kozmoai_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from kozmoai_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFGrowthTechEquitiesQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Growth Tech Stocks Query.

    Source: https://finance.yahoo.com/screener/predefined/growth_technology_stocks
    """

    limit: Optional[int] = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFGrowthTechEquitiesData(YFPredefinedScreenerData):
    """Yahoo Finance Growth Tech Stocks Data."""


class YFGrowthTechEquitiesFetcher(
    Fetcher[YFGrowthTechEquitiesQueryParams, list[YFGrowthTechEquitiesData]]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFGrowthTechEquitiesQueryParams:
        """Transform query params."""
        return YFGrowthTechEquitiesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFGrowthTechEquitiesQueryParams,
        credentials: Optional[dict[str, str]],
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from kozmoai_yfinance.utils.helpers import get_defined_screener

        return await get_defined_screener(
            name="growth_technology_stocks", limit=query.limit
        )

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFGrowthTechEquitiesData]:
        """Transform data."""
        return [
            YFGrowthTechEquitiesData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]
