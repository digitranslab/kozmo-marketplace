"""Yahoo Finance Asset Undervalued Large Caps Model."""

# pylint: disable=unused-argument

from typing import Any, Optional

from kozmoai_core.provider.abstract.fetcher import Fetcher
from kozmoai_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from kozmoai_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFUndervaluedLargeCapsQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Undervalued Large Caps Query.

    Source: https://finance.yahoo.com/screener/predefined/undervalued_large_caps
    """

    limit: Optional[int] = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFUndervaluedLargeCapsData(YFPredefinedScreenerData):
    """Yahoo Finance Undervalued Large Caps Data."""


class YFUndervaluedLargeCapsFetcher(
    Fetcher[YFUndervaluedLargeCapsQueryParams, list[YFUndervaluedLargeCapsData]]
):
    """Yahoo Finance Undervalued Large Caps Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFUndervaluedLargeCapsQueryParams:
        """Transform query params."""
        return YFUndervaluedLargeCapsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFUndervaluedLargeCapsQueryParams,
        credentials: Optional[dict[str, str]],
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from kozmoai_yfinance.utils.helpers import get_defined_screener

        return await get_defined_screener(
            name="undervalued_large_caps", limit=query.limit
        )

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFUndervaluedLargeCapsData]:
        """Transform data."""
        return [
            YFUndervaluedLargeCapsData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]
