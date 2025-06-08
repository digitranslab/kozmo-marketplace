"""TMX Provider Module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_tmx.models.available_indices import TmxAvailableIndicesFetcher
from kozmoai_tmx.models.bond_prices import TmxBondPricesFetcher
from kozmoai_tmx.models.calendar_earnings import TmxCalendarEarningsFetcher
from kozmoai_tmx.models.company_filings import TmxCompanyFilingsFetcher
from kozmoai_tmx.models.company_news import TmxCompanyNewsFetcher
from kozmoai_tmx.models.equity_historical import TmxEquityHistoricalFetcher
from kozmoai_tmx.models.equity_profile import TmxEquityProfileFetcher
from kozmoai_tmx.models.equity_quote import TmxEquityQuoteFetcher
from kozmoai_tmx.models.equity_search import TmxEquitySearchFetcher
from kozmoai_tmx.models.etf_countries import TmxEtfCountriesFetcher
from kozmoai_tmx.models.etf_holdings import TmxEtfHoldingsFetcher
from kozmoai_tmx.models.etf_info import TmxEtfInfoFetcher
from kozmoai_tmx.models.etf_search import TmxEtfSearchFetcher
from kozmoai_tmx.models.etf_sectors import TmxEtfSectorsFetcher
from kozmoai_tmx.models.gainers import TmxGainersFetcher
from kozmoai_tmx.models.historical_dividends import TmxHistoricalDividendsFetcher
from kozmoai_tmx.models.index_constituents import TmxIndexConstituentsFetcher
from kozmoai_tmx.models.index_sectors import TmxIndexSectorsFetcher
from kozmoai_tmx.models.index_snapshots import TmxIndexSnapshotsFetcher
from kozmoai_tmx.models.insider_trading import TmxInsiderTradingFetcher
from kozmoai_tmx.models.options_chains import TmxOptionsChainsFetcher
from kozmoai_tmx.models.price_target_consensus import TmxPriceTargetConsensusFetcher
from kozmoai_tmx.models.treasury_prices import TmxTreasuryPricesFetcher

tmx_provider = Provider(
    name="tmx",
    website="https://www.tmx.com",
    description="""Unofficial TMX Data Provider Extension
    TMX Group Companies
        - Toronto Stock Exchange
        - TSX Venture Exchange
        - TSX Trust
        - Montréal Exchange
        - TSX Alpha Exchange
        - Shorcan
        - CDCC
        - CDS
        - TMX Datalinx
        - Trayport
    """,
    fetcher_dict={
        "AvailableIndices": TmxAvailableIndicesFetcher,
        "BondPrices": TmxBondPricesFetcher,
        "CalendarEarnings": TmxCalendarEarningsFetcher,
        "CompanyFilings": TmxCompanyFilingsFetcher,
        "CompanyNews": TmxCompanyNewsFetcher,
        "EquityHistorical": TmxEquityHistoricalFetcher,
        "EquityInfo": TmxEquityProfileFetcher,
        "EquityQuote": TmxEquityQuoteFetcher,
        "EquitySearch": TmxEquitySearchFetcher,
        "EtfSearch": TmxEtfSearchFetcher,
        "EtfHoldings": TmxEtfHoldingsFetcher,
        "EtfSectors": TmxEtfSectorsFetcher,
        "EtfCountries": TmxEtfCountriesFetcher,
        "EtfHistorical": TmxEquityHistoricalFetcher,
        "EtfInfo": TmxEtfInfoFetcher,
        "EquityGainers": TmxGainersFetcher,
        "HistoricalDividends": TmxHistoricalDividendsFetcher,
        "IndexConstituents": TmxIndexConstituentsFetcher,
        "IndexSectors": TmxIndexSectorsFetcher,
        "IndexSnapshots": TmxIndexSnapshotsFetcher,
        "InsiderTrading": TmxInsiderTradingFetcher,
        "OptionsChains": TmxOptionsChainsFetcher,
        "PriceTargetConsensus": TmxPriceTargetConsensusFetcher,
        "TreasuryPrices": TmxTreasuryPricesFetcher,
    },
    repr_name="TMX",
)
