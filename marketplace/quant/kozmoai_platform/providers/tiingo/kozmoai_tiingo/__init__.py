"""Tiingo provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_tiingo.models.company_news import TiingoCompanyNewsFetcher
from kozmoai_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from kozmoai_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from kozmoai_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from kozmoai_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from kozmoai_tiingo.models.world_news import TiingoWorldNewsFetcher

tiingo_provider = Provider(
    name="tiingo",
    website="https://tiingo.com",
    description="""A Reliable, Enterprise-Grade Financial Markets API. Tiingo's APIs
power hedge funds, tech companies, and individuals.""",
    credentials=["token"],
    fetcher_dict={
        "EquityHistorical": TiingoEquityHistoricalFetcher,
        "EtfHistorical": TiingoEquityHistoricalFetcher,
        "CompanyNews": TiingoCompanyNewsFetcher,
        "WorldNews": TiingoWorldNewsFetcher,
        "CryptoHistorical": TiingoCryptoHistoricalFetcher,
        "CurrencyHistorical": TiingoCurrencyHistoricalFetcher,
        "TrailingDividendYield": TiingoTrailingDivYieldFetcher,
    },
    repr_name="Tiingo",
)
