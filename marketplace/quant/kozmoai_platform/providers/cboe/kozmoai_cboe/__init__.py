"""Cboe provider module."""

from kozmoai_cboe.models.available_indices import CboeAvailableIndicesFetcher
from kozmoai_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from kozmoai_cboe.models.equity_quote import CboeEquityQuoteFetcher
from kozmoai_cboe.models.equity_search import CboeEquitySearchFetcher
from kozmoai_cboe.models.futures_curve import CboeFuturesCurveFetcher
from kozmoai_cboe.models.index_constituents import (
    CboeIndexConstituentsFetcher,
)
from kozmoai_cboe.models.index_historical import (
    CboeIndexHistoricalFetcher,
)
from kozmoai_cboe.models.index_search import CboeIndexSearchFetcher
from kozmoai_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from kozmoai_cboe.models.options_chains import CboeOptionsChainsFetcher
from kozmoai_core.provider.abstract.provider import Provider

cboe_provider = Provider(
    name="cboe",
    website="https://www.cboe.com",
    description="""Cboe is the world's go-to derivatives and exchange network,
delivering cutting-edge trading, clearing and investment solutions to people
around the world.""",
    credentials=None,
    fetcher_dict={
        "AvailableIndices": CboeAvailableIndicesFetcher,
        "EquityHistorical": CboeEquityHistoricalFetcher,
        "EquityQuote": CboeEquityQuoteFetcher,
        "EquitySearch": CboeEquitySearchFetcher,
        "EtfHistorical": CboeEquityHistoricalFetcher,
        "IndexConstituents": CboeIndexConstituentsFetcher,
        "FuturesCurve": CboeFuturesCurveFetcher,
        "IndexHistorical": CboeIndexHistoricalFetcher,
        "IndexSearch": CboeIndexSearchFetcher,
        "IndexSnapshots": CboeIndexSnapshotsFetcher,
        "OptionsChains": CboeOptionsChainsFetcher,
    },
    repr_name="Chicago Board Options Exchange (CBOE)",
)
