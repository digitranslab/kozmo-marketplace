"""Price Router."""

# pylint: disable=unused-argument

from kozmoai_core.app.model.command_context import CommandContext
from kozmoai_core.app.model.example import APIEx
from kozmoai_core.app.model.obbject import OBBject
from kozmoai_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from kozmoai_core.app.query import Query
from kozmoai_core.app.router import Router

router = Router(prefix="/price")


@router.command(
    model="CommoditySpotPrices",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"provider": "fred", "commodity": "wti"}),
    ],
)
async def spot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Commodity Spot Prices."""
    return await OBBject.from_query(Query(**locals()))
