"""Benzinga Helpers."""

from kozmoai_core.app.model.abstract.error import KozmoAIError
from kozmoai_core.provider.utils.errors import EmptyDataError, UnauthorizedError


async def response_callback(response, _):
    """Response callback."""
    # pylint: disable=import-outside-toplevel
    results = await response.json()
    if (
        results
        and isinstance(results, list)
        and len(results) == 1
        and isinstance(results[0], str)
    ):
        if "access denied" in results[0].lower():
            raise UnauthorizedError(f"Unauthorized Benzinga request -> {results[0]}")
        raise KozmoAIError(results[0])

    if isinstance(results, list) and not results:
        raise EmptyDataError("The request was returned empty.")

    return results
