"""Yahoo Finance provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_yfinance.models.active import YFActiveFetcher
from kozmoai_yfinance.models.aggressive_small_caps import YFAggressiveSmallCapsFetcher
from kozmoai_yfinance.models.available_indices import YFinanceAvailableIndicesFetcher
from kozmoai_yfinance.models.balance_sheet import YFinanceBalanceSheetFetcher
from kozmoai_yfinance.models.cash_flow import YFinanceCashFlowStatementFetcher
from kozmoai_yfinance.models.company_news import YFinanceCompanyNewsFetcher
from kozmoai_yfinance.models.crypto_historical import YFinanceCryptoHistoricalFetcher
from kozmoai_yfinance.models.currency_historical import YFinanceCurrencyHistoricalFetcher
from kozmoai_yfinance.models.equity_historical import YFinanceEquityHistoricalFetcher
from kozmoai_yfinance.models.equity_profile import YFinanceEquityProfileFetcher
from kozmoai_yfinance.models.equity_quote import YFinanceEquityQuoteFetcher
from kozmoai_yfinance.models.equity_screener import YFinanceEquityScreenerFetcher
from kozmoai_yfinance.models.etf_info import YFinanceEtfInfoFetcher
from kozmoai_yfinance.models.futures_curve import YFinanceFuturesCurveFetcher
from kozmoai_yfinance.models.futures_historical import YFinanceFuturesHistoricalFetcher
from kozmoai_yfinance.models.gainers import YFGainersFetcher
from kozmoai_yfinance.models.growth_tech_equities import YFGrowthTechEquitiesFetcher
from kozmoai_yfinance.models.historical_dividends import (
    YFinanceHistoricalDividendsFetcher,
)
from kozmoai_yfinance.models.income_statement import YFinanceIncomeStatementFetcher
from kozmoai_yfinance.models.index_historical import (
    YFinanceIndexHistoricalFetcher,
)
from kozmoai_yfinance.models.key_executives import YFinanceKeyExecutivesFetcher
from kozmoai_yfinance.models.key_metrics import YFinanceKeyMetricsFetcher
from kozmoai_yfinance.models.losers import YFLosersFetcher
from kozmoai_yfinance.models.options_chains import YFinanceOptionsChainsFetcher
from kozmoai_yfinance.models.price_target_consensus import (
    YFinancePriceTargetConsensusFetcher,
)
from kozmoai_yfinance.models.share_statistics import YFinanceShareStatisticsFetcher
from kozmoai_yfinance.models.undervalued_growth_equities import (
    YFUndervaluedGrowthEquitiesFetcher,
)
from kozmoai_yfinance.models.undervalued_large_caps import YFUndervaluedLargeCapsFetcher

yfinance_provider = Provider(
    name="yfinance",
    website="https://finance.yahoo.com",
    description="""Yahoo! Finance is a web-based platform that offers financial news,
data, and tools for investors and individuals interested in tracking and analyzing
financial markets and assets.""",
    fetcher_dict={
        "AvailableIndices": YFinanceAvailableIndicesFetcher,
        "BalanceSheet": YFinanceBalanceSheetFetcher,
        "CashFlowStatement": YFinanceCashFlowStatementFetcher,
        "CompanyNews": YFinanceCompanyNewsFetcher,
        "CryptoHistorical": YFinanceCryptoHistoricalFetcher,
        "CurrencyHistorical": YFinanceCurrencyHistoricalFetcher,
        "EquityActive": YFActiveFetcher,
        "EquityAggressiveSmallCaps": YFAggressiveSmallCapsFetcher,
        "EquityGainers": YFGainersFetcher,
        "EquityHistorical": YFinanceEquityHistoricalFetcher,
        "EquityInfo": YFinanceEquityProfileFetcher,
        "EquityLosers": YFLosersFetcher,
        "EquityQuote": YFinanceEquityQuoteFetcher,
        "EquityScreener": YFinanceEquityScreenerFetcher,
        "EquityUndervaluedGrowth": YFUndervaluedGrowthEquitiesFetcher,
        "EquityUndervaluedLargeCaps": YFUndervaluedLargeCapsFetcher,
        "EtfHistorical": YFinanceEquityHistoricalFetcher,
        "EtfInfo": YFinanceEtfInfoFetcher,
        "FuturesCurve": YFinanceFuturesCurveFetcher,
        "FuturesHistorical": YFinanceFuturesHistoricalFetcher,
        "GrowthTechEquities": YFGrowthTechEquitiesFetcher,
        "HistoricalDividends": YFinanceHistoricalDividendsFetcher,
        "IncomeStatement": YFinanceIncomeStatementFetcher,
        "IndexHistorical": YFinanceIndexHistoricalFetcher,
        "KeyExecutives": YFinanceKeyExecutivesFetcher,
        "KeyMetrics": YFinanceKeyMetricsFetcher,
        "OptionsChains": YFinanceOptionsChainsFetcher,
        "PriceTargetConsensus": YFinancePriceTargetConsensusFetcher,
        "ShareStatistics": YFinanceShareStatisticsFetcher,
    },
    repr_name="Yahoo Finance",
)
