"""Price Router."""

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

# pylint: disable=unused-argument


@router.command(
    model="IndexHistorical",
    examples=[
        APIEx(parameters={"symbol": "^GSPC", "provider": "fmp"}),
        APIEx(
            description="Not all providers have the same symbols.",
            parameters={"symbol": "SPX", "provider": "intrinio"},
        ),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Historical Index Levels."""
    return await OBBject.from_query(Query(**locals()))
