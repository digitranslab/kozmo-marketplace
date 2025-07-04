"""Coverage dependency."""

from fastapi import Depends
from kozmoai_core.app.provider_interface import ProviderInterface
from kozmoai_core.app.router import CommandMap
from kozmoai_core.app.service.auth_service import AuthService
from typing_extensions import Annotated


async def get_command_map(
    _: Annotated[None, Depends(AuthService().auth_hook)]
) -> CommandMap:
    """Get command map."""
    return CommandMap()


async def get_provider_interface(
    _: Annotated[None, Depends(AuthService().auth_hook)]
) -> ProviderInterface:
    """Get provider interface."""
    return ProviderInterface()
