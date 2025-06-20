"""Finviz provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_finviz.models.compare_groups import FinvizCompareGroupsFetcher
from kozmoai_finviz.models.equity_profile import FinvizEquityProfileFetcher
from kozmoai_finviz.models.equity_screener import FinvizEquityScreenerFetcher
from kozmoai_finviz.models.key_metrics import FinvizKeyMetricsFetcher
from kozmoai_finviz.models.price_performance import FinvizPricePerformanceFetcher
from kozmoai_finviz.models.price_target import FinvizPriceTargetFetcher

finviz_provider = Provider(
    name="finviz",
    website="https://finviz.com",
    description="Unofficial Finviz API - https://github.com/lit26/finvizfinance/releases",
    credentials=None,
    fetcher_dict={
        "CompareGroups": FinvizCompareGroupsFetcher,
        "EtfPricePerformance": FinvizPricePerformanceFetcher,
        "EquityInfo": FinvizEquityProfileFetcher,
        "EquityScreener": FinvizEquityScreenerFetcher,
        "KeyMetrics": FinvizKeyMetricsFetcher,
        "PricePerformance": FinvizPricePerformanceFetcher,
        "PriceTarget": FinvizPriceTargetFetcher,
    },
    repr_name="FinViz",
)
