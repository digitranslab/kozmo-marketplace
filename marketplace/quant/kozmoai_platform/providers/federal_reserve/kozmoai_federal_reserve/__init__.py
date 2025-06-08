"""Federal Reserve provider module."""

from kozmoai_core.provider.abstract.provider import Provider
from kozmoai_federal_reserve.models.central_bank_holdings import (
    FederalReserveCentralBankHoldingsFetcher,
)
from kozmoai_federal_reserve.models.federal_funds_rate import (
    FederalReserveFederalFundsRateFetcher,
)
from kozmoai_federal_reserve.models.money_measures import (
    FederalReserveMoneyMeasuresFetcher,
)
from kozmoai_federal_reserve.models.overnight_bank_funding_rate import (
    FederalReserveOvernightBankFundingRateFetcher,
)
from kozmoai_federal_reserve.models.primary_dealer_fails import (
    FederalReservePrimaryDealerFailsFetcher,
)
from kozmoai_federal_reserve.models.primary_dealer_positioning import (
    FederalReservePrimaryDealerPositioningFetcher,
)
from kozmoai_federal_reserve.models.sofr import FederalReserveSOFRFetcher
from kozmoai_federal_reserve.models.treasury_rates import (
    FederalReserveTreasuryRatesFetcher,
)
from kozmoai_federal_reserve.models.yield_curve import FederalReserveYieldCurveFetcher

federal_reserve_provider = Provider(
    name="federal_reserve",
    website="https://www.federalreserve.gov/data.htm",  #  Not a typo, it's really .htm
    description="""Access data provided by the Federal Reserve System, the Central Bank of the United States.""",
    fetcher_dict={
        "CentralBankHoldings": FederalReserveCentralBankHoldingsFetcher,
        "FederalFundsRate": FederalReserveFederalFundsRateFetcher,
        "MoneyMeasures": FederalReserveMoneyMeasuresFetcher,
        "OvernightBankFundingRate": FederalReserveOvernightBankFundingRateFetcher,
        "PrimaryDealerFails": FederalReservePrimaryDealerFailsFetcher,
        "PrimaryDealerPositioning": FederalReservePrimaryDealerPositioningFetcher,
        "SOFR": FederalReserveSOFRFetcher,
        "TreasuryRates": FederalReserveTreasuryRatesFetcher,
        "YieldCurve": FederalReserveYieldCurveFetcher,
    },
    repr_name="Federal Reserve (FED)",
)
