"""Benzinga provider module."""

from kozmoai_benzinga.models.analyst_search import BenzingaAnalystSearchFetcher
from kozmoai_benzinga.models.company_news import BenzingaCompanyNewsFetcher
from kozmoai_benzinga.models.price_target import BenzingaPriceTargetFetcher
from kozmoai_benzinga.models.world_news import BenzingaWorldNewsFetcher
from kozmoai_core.provider.abstract.provider import Provider

benzinga_provider = Provider(
    name="benzinga",
    website="https://www.benzinga.com",
    description="""Benzinga is a financial data provider that offers an API
focused on information that moves the market.""",
    credentials=["api_key"],
    fetcher_dict={
        "AnalystSearch": BenzingaAnalystSearchFetcher,
        "CompanyNews": BenzingaCompanyNewsFetcher,
        "WorldNews": BenzingaWorldNewsFetcher,
        "PriceTarget": BenzingaPriceTargetFetcher,
    },
    repr_name="Benzinga",
)
