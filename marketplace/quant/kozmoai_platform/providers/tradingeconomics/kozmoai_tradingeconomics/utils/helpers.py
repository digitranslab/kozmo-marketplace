"""TradingEconomics Helpers."""

from typing import Union

from kozmoai_core.app.model.abstract.error import KozmoAIError
from kozmoai_core.provider.utils.errors import EmptyDataError, UnauthorizedError


async def response_callback(response, _) -> Union[dict, list[dict]]:
    """Return the response."""
    if response.status != 200:
        message = await response.text()

        if "credentials" in message or "unauthorized" in message.lower():
            raise UnauthorizedError(
                f"Unauthorized TradingEconomics request -> {message}"
            )

        raise KozmoAIError(f"{response.status} -> {message}")

    results = await response.json()

    if not results:
        raise EmptyDataError("The request was returned empty.")

    return results
