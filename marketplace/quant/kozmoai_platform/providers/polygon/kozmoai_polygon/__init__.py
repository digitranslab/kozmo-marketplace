"""Polygon provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_polygon.models.balance_sheet import PolygonBalanceSheetFetcher
from kozmoai_polygon.models.cash_flow import PolygonCashFlowStatementFetcher
from kozmoai_polygon.models.company_news import PolygonCompanyNewsFetcher
from kozmoai_polygon.models.crypto_historical import PolygonCryptoHistoricalFetcher
from kozmoai_polygon.models.currency_historical import PolygonCurrencyHistoricalFetcher
from kozmoai_polygon.models.currency_pairs import PolygonCurrencyPairsFetcher
from kozmoai_polygon.models.currency_snapshots import PolygonCurrencySnapshotsFetcher
from kozmoai_polygon.models.equity_historical import PolygonEquityHistoricalFetcher
from kozmoai_polygon.models.equity_nbbo import PolygonEquityNBBOFetcher
from kozmoai_polygon.models.income_statement import PolygonIncomeStatementFetcher
from kozmoai_polygon.models.index_historical import (
    PolygonIndexHistoricalFetcher,
)
from kozmoai_polygon.models.market_snapshots import PolygonMarketSnapshotsFetcher

polygon_provider = Provider(
    name="polygon",
    website="https://polygon.io",
    description="""The Polygon.io Stocks API provides REST endpoints that let you query
the latest market data from all US stock exchanges. You can also find data on
company financials, stock market holidays, corporate actions, and more.""",
    credentials=["api_key"],
    fetcher_dict={
        "BalanceSheet": PolygonBalanceSheetFetcher,
        "CashFlowStatement": PolygonCashFlowStatementFetcher,
        "CompanyNews": PolygonCompanyNewsFetcher,
        "CryptoHistorical": PolygonCryptoHistoricalFetcher,
        "CurrencyHistorical": PolygonCurrencyHistoricalFetcher,
        "CurrencyPairs": PolygonCurrencyPairsFetcher,
        "CurrencySnapshots": PolygonCurrencySnapshotsFetcher,
        "EquityHistorical": PolygonEquityHistoricalFetcher,
        "EquityNBBO": PolygonEquityNBBOFetcher,
        "EtfHistorical": PolygonEquityHistoricalFetcher,
        "IncomeStatement": PolygonIncomeStatementFetcher,
        "IndexHistorical": PolygonIndexHistoricalFetcher,
        "MarketSnapshots": PolygonMarketSnapshotsFetcher,
    },
    repr_name="Polygon.io",
    deprecated_credentials={"API_POLYGON_KEY": "polygon_api_key"},
    instructions='Go to: https://polygon.io\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207825623-fcd7f0a3-131a-4294-808c-754c13e38e2a.png)\n\nClick on, "Get your Free API Key".\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207825952-ca5540ec-6ed2-4cef-a0ed-bb50b813932c.png)\n\nAfter signing up, the API Key is found at the bottom of the account dashboard page.\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207826258-b1f318fa-fd9c-41d9-bf5c-fe16722e6601.png)',  # noqa: E501  pylint: disable=line-too-long
)
