"""Test Intrinio fetchers."""

from datetime import date
from unittest import mock

import pytest
from kozmoai_core.app.service.user_service import UserService
from kozmoai_intrinio.models.balance_sheet import IntrinioBalanceSheetFetcher
from kozmoai_intrinio.models.calendar_ipo import IntrinioCalendarIpoFetcher
from kozmoai_intrinio.models.cash_flow import IntrinioCashFlowStatementFetcher
from kozmoai_intrinio.models.company_filings import IntrinioCompanyFilingsFetcher
from kozmoai_intrinio.models.company_news import IntrinioCompanyNewsFetcher
from kozmoai_intrinio.models.currency_pairs import IntrinioCurrencyPairsFetcher
from kozmoai_intrinio.models.equity_historical import IntrinioEquityHistoricalFetcher
from kozmoai_intrinio.models.equity_info import IntrinioEquityInfoFetcher
from kozmoai_intrinio.models.equity_quote import IntrinioEquityQuoteFetcher
from kozmoai_intrinio.models.equity_search import IntrinioEquitySearchFetcher
from kozmoai_intrinio.models.etf_holdings import IntrinioEtfHoldingsFetcher
from kozmoai_intrinio.models.etf_info import IntrinioEtfInfoFetcher
from kozmoai_intrinio.models.etf_price_performance import (
    IntrinioEtfPricePerformanceFetcher,
)
from kozmoai_intrinio.models.etf_search import IntrinioEtfSearchFetcher
from kozmoai_intrinio.models.financial_ratios import IntrinioFinancialRatiosFetcher
from kozmoai_intrinio.models.forward_ebitda_estimates import (
    IntrinioForwardEbitdaEstimatesFetcher,
)
from kozmoai_intrinio.models.forward_eps_estimates import (
    IntrinioForwardEpsEstimatesFetcher,
)
from kozmoai_intrinio.models.forward_pe_estimates import (
    IntrinioForwardPeEstimatesFetcher,
)
from kozmoai_intrinio.models.forward_sales_estimates import (
    IntrinioForwardSalesEstimatesFetcher,
)
from kozmoai_intrinio.models.fred_series import IntrinioFredSeriesFetcher
from kozmoai_intrinio.models.historical_attributes import (
    IntrinioHistoricalAttributesFetcher,
)
from kozmoai_intrinio.models.historical_dividends import (
    IntrinioHistoricalDividendsFetcher,
)
from kozmoai_intrinio.models.historical_market_cap import (
    IntrinioHistoricalMarketCapFetcher,
)
from kozmoai_intrinio.models.income_statement import IntrinioIncomeStatementFetcher
from kozmoai_intrinio.models.index_historical import IntrinioIndexHistoricalFetcher
from kozmoai_intrinio.models.insider_trading import IntrinioInsiderTradingFetcher

# from kozmoai_intrinio.models.institutional_ownership import (
#     IntrinioInstitutionalOwnershipFetcher,
# )
from kozmoai_intrinio.models.key_metrics import IntrinioKeyMetricsFetcher
from kozmoai_intrinio.models.latest_attributes import IntrinioLatestAttributesFetcher
from kozmoai_intrinio.models.market_snapshots import IntrinioMarketSnapshotsFetcher
from kozmoai_intrinio.models.options_chains import IntrinioOptionsChainsFetcher
from kozmoai_intrinio.models.options_snapshots import IntrinioOptionsSnapshotsFetcher
from kozmoai_intrinio.models.options_unusual import IntrinioOptionsUnusualFetcher
from kozmoai_intrinio.models.price_target_consensus import (
    IntrinioPriceTargetConsensusFetcher,
)
from kozmoai_intrinio.models.reported_financials import IntrinioReportedFinancialsFetcher
from kozmoai_intrinio.models.search_attributes import (
    IntrinioSearchAttributesFetcher,
)
from kozmoai_intrinio.models.share_statistics import IntrinioShareStatisticsFetcher
from kozmoai_intrinio.models.world_news import IntrinioWorldNewsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("api_key", "MOCK_API_KEY"),
            ("X-Amz-Algorithm", "MOCK_X-Amz-Algorithm"),
            ("X-Amz-Credential", "MOCK_X-Amz-Credential"),
            ("X-Amz-Date", "MOCK_X-Amz-Date"),
            ("X-Amz-Expires", "MOCK_X-Amz-Expires"),
            ("X-Amz-SignedHeaders", "MOCK_X-Amz-SignedHeaders"),
            ("X-Amz-Signature", "MOCK_X-Amz-Signature"),
        ],
    }


@pytest.fixture(autouse=True, scope="module")
def mock_cpu_count():
    """Mock the cpu_count function so recording works."""
    with mock.patch(
        "os.cpu_count"
    ) as mock_cpu_count:  # pylint: disable=redefined-outer-name
        mock_cpu_count.return_value = -3
        yield


@pytest.mark.record_http
def test_intrinio_equity_historical_fetcher(credentials=test_credentials):
    """Test equity historical fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "1d",
    }

    fetcher = IntrinioEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_currency_pairs_fetcher(credentials=test_credentials):
    """Test currency pairs fetcher."""
    params = {}

    fetcher = IntrinioCurrencyPairsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_company_news_fetcher(credentials=test_credentials):
    """Test company news fetcher."""
    params = {
        "symbol": "AAPL",
        "limit": 50,
        "source": "yahoo",
        "start_date": date(2024, 1, 2),
        "end_date": date(2024, 1, 3),
    }

    fetcher = IntrinioCompanyNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_world_news_fetcher(credentials=test_credentials):
    """Test world news fetcher."""
    params = {
        "limit": 50,
        "source": "yahoo",
        "start_date": date(2024, 1, 2),
        "end_date": date(2024, 1, 3),
    }

    fetcher = IntrinioWorldNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_equity_quote_fetcher(credentials=test_credentials):
    """Test equity quote fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioEquityQuoteFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_options_chains_fetcher(credentials=test_credentials):
    """Test options chains fetcher."""

    params = {"symbol": "AAPL", "date": date(2023, 9, 15), "delay": "eod"}

    fetcher = IntrinioOptionsChainsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_options_unusual_fetcher(credentials=test_credentials):
    """Test options unusual fetcher."""
    params = {
        "source": "delayed",
        "trade_type": "block",
        "sentiment": "neutral",
        "start_date": date(2023, 11, 20),
        "min_value": 10000000,
    }

    fetcher = IntrinioOptionsUnusualFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_balance_sheet_fetcher(credentials=test_credentials):
    """Test balance sheet fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioBalanceSheetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_cash_flow_statement_fetcher(credentials=test_credentials):
    """Test cash flow statement fetcher."""
    params = {"symbol": "AAPL"}
    fetcher = IntrinioCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_income_statement_fetcher(credentials=test_credentials):
    """Test income statement fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioIncomeStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_fred_series_fetcher(credentials=test_credentials):
    """Test fred series fetcher."""
    params = {
        "symbol": "$GDP",
        "start_date": date(2022, 9, 20),
        "end_date": date(2023, 9, 20),
    }

    fetcher = IntrinioFredSeriesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_calendar_ipo_fetcher(credentials=test_credentials):
    """Test calendar IPO fetcher."""
    params = {"status": "upcoming"}

    fetcher = IntrinioCalendarIpoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_search_attributes(credentials=test_credentials):
    """Test search attributes fetcher."""
    params = {"query": "ebit"}

    fetcher = IntrinioSearchAttributesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_historical_attributes(credentials=test_credentials):
    """Test historical attributes fetcher."""
    params = {
        "provider": "intrinio",
        "symbol": "AAPL,MSFT",
        "tag": "ebit,marketcap",
        "frequency": "yearly",
        "limit": 1000,
        "tag_type": None,
        "start_date": date(2013, 1, 1),
        "end_date": date(2023, 1, 1),
        "sort": "desc",
    }

    fetcher = IntrinioHistoricalAttributesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_latest_attributes(credentials=test_credentials):
    """Test latest attributes fetcher."""
    params = {
        "provider": "intrinio",
        "symbol": "AAPL,MSFT",
        "tag": "ceo,marketcap",
    }

    fetcher = IntrinioLatestAttributesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_equity_info_fetcher(credentials=test_credentials):
    """Test equity info fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioEquityInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_index_historical_fetcher(credentials=test_credentials):
    """Test index historical fetcher."""
    params = {
        "symbol": "DJI",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 2, 5),
    }

    fetcher = IntrinioIndexHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_historical_dividends_fetcher(credentials=test_credentials):
    """Test historical dividends fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = IntrinioHistoricalDividendsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_company_filings_fetcher(credentials=test_credentials):
    """Test company filings fetcher."""
    params = {
        "symbol": "AAPL",
        "form_type": None,
        "limit": 100,
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = IntrinioCompanyFilingsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_insider_trading_fetcher(credentials=test_credentials):
    """Test insider trading fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = IntrinioInsiderTradingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# Disabled due to unreliable Intrinio endpoint
# @pytest.mark.record_http
# def test_intrinio_institutional_ownership_fetcher(credentials=test_credentials):
#     params = {"symbol": "AAPL"}

#     fetcher = IntrinioInstitutionalOwnershipFetcher()
#     result = fetcher.test(params, credentials)
#     assert result is None


@pytest.mark.record_http
def test_intrinio_key_metrics_fetcher(credentials=test_credentials):
    """Test key metrics fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioKeyMetricsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_share_statistics_fetcher(credentials=test_credentials):
    """Test share statistics fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioShareStatisticsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_equity_search_fetcher(credentials=test_credentials):
    """Test equity search fetcher."""
    params = {"query": "gold", "limit": 100}

    fetcher = IntrinioEquitySearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_financial_ratios_fetcher(credentials=test_credentials):
    """Test financial ratios fetcher."""
    params = {"symbol": "AAPL", "period": "annual", "limit": 2, "use_cache": False}

    fetcher = IntrinioFinancialRatiosFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_reported_financials_fetcher(credentials=test_credentials):
    """Test reported financials fetcher."""
    params = {
        "symbol": "AAPL",
        "statement_type": "cash",
        "period": "quarter",
        "limit": 1,
    }

    fetcher = IntrinioReportedFinancialsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_etf_search_fetcher(credentials=test_credentials):
    """Test etf search fetcher."""
    params = {"query": "factor", "exchange": "bats"}

    fetcher = IntrinioEtfSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_etf_info_fetcher(credentials=test_credentials):
    """Test etf info fetcher."""
    params = {"symbol": "DJIA,SPY,GOVT"}

    fetcher = IntrinioEtfInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_etf_holdings_fetcher(credentials=test_credentials):
    """Test etf holdings fetcher."""
    params = {"symbol": "DJIA"}

    fetcher = IntrinioEtfHoldingsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_etf_price_performance_fetcher(credentials=test_credentials):
    """Test etf price performance fetcher."""
    params = {"symbol": "SPY:US"}

    fetcher = IntrinioEtfPricePerformanceFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_market_snapshots_fetcher(credentials=test_credentials):
    """Test market snapshots fetcher."""
    params = {"date": date(2022, 6, 30)}

    fetcher = IntrinioMarketSnapshotsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_forward_eps_estimates_fetcher(credentials=test_credentials):
    """Test forward EPS estimates fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioForwardEpsEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_forward_sales_estimates_fetcher(credentials=test_credentials):
    """Test forward sales estimates fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioForwardSalesEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_price_target_consensus_fetcher(credentials=test_credentials):
    """Test price target consensus fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = IntrinioPriceTargetConsensusFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_forward_pe_fetcher(credentials=test_credentials):
    """Test forward pe fetcher."""
    params = {"symbol": "AAPL,MSFT"}

    fetcher = IntrinioForwardPeEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_forward_ebitda_fetcher(credentials=test_credentials):
    """Test forward ebitda fetcher."""
    params = {"symbol": "AAPL,MSFT"}

    fetcher = IntrinioForwardEbitdaEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.skip(reason="HTTP request is too large and unreasonable to store.")
def test_intrinio_options_snapshots(credentials=test_credentials):
    """Test options snapshots fetcher."""
    params = {"date": "2024-06-11"}

    fetcher = IntrinioOptionsSnapshotsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_intrinio_historical_market_cap(credentials=test_credentials):
    """Test options snapshots fetcher."""
    params = {
        "symbol": "AAPL,MSFT",
        "start_date": date(2020, 1, 1),
        "end_date": date(2020, 12, 31),
        "interval": "week",
    }

    fetcher = IntrinioHistoricalMarketCapFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
