"""Nasdaq provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_nasdaq.models.calendar_dividend import NasdaqCalendarDividendFetcher
from kozmoai_nasdaq.models.calendar_earnings import NasdaqCalendarEarningsFetcher
from kozmoai_nasdaq.models.calendar_ipo import NasdaqCalendarIpoFetcher
from kozmoai_nasdaq.models.economic_calendar import NasdaqEconomicCalendarFetcher
from kozmoai_nasdaq.models.equity_screener import NasdaqEquityScreenerFetcher
from kozmoai_nasdaq.models.equity_search import NasdaqEquitySearchFetcher
from kozmoai_nasdaq.models.historical_dividends import NasdaqHistoricalDividendsFetcher
from kozmoai_nasdaq.models.top_retail import NasdaqTopRetailFetcher

nasdaq_provider = Provider(
    name="nasdaq",
    website="https://data.nasdaq.com",
    description="""Positioned at the nexus of technology and the capital markets, Nasdaq
provides premier platforms and services for global capital markets and beyond with
unmatched technology, insights and markets expertise.""",
    credentials=["api_key"],
    fetcher_dict={
        "CalendarDividend": NasdaqCalendarDividendFetcher,
        "CalendarEarnings": NasdaqCalendarEarningsFetcher,
        "CalendarIpo": NasdaqCalendarIpoFetcher,
        "EconomicCalendar": NasdaqEconomicCalendarFetcher,
        "EquitySearch": NasdaqEquitySearchFetcher,
        "EquityScreener": NasdaqEquityScreenerFetcher,
        "HistoricalDividends": NasdaqHistoricalDividendsFetcher,
        "TopRetail": NasdaqTopRetailFetcher,
    },
    repr_name="NASDAQ",
    deprecated_credentials={"API_KEY_QUANDL": "nasdaq_api_key"},
    instructions='Go to: https://www.quandl.com\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207823899-208a3952-f557-4b73-aee6-64ac00faedb7.png)\n\nClick on, "Sign Up", and register a new account.\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207824214-4b6b2b74-e709-4ed4-adf2-14803e6f3568.png)\n\nFollow the sign-up instructions, and upon completion the API key will be assigned.\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207824664-3c82befb-9c69-42df-8a82-510d85c19a97.png)',  # noqa: E501  pylint: disable=line-too-long
)
