"""IMF Helper Utilities."""


async def get_data(url: str) -> list[dict]:
    """Get data from the IMF API."""
    # pylint: disable=import-outside-toplevel

    from aiohttp.client_exceptions import ContentTypeError  # noqa
    from json.decoder import JSONDecodeError
    from kozmoai_core.provider.utils.helpers import amake_request
    from kozmoai_core.app.model.abstract.error import KozmoAIError

    try:
        response = await amake_request(url, timeout=20)
    except (JSONDecodeError, ContentTypeError) as e:
        raise KozmoAIError(
            "Error fetching data; This might be rate-limiting. Try again later."
        ) from e

    if "ErrorDetails" in response:
        raise KozmoAIError(
            f"{response['ErrorDetails'].get('Code')} -> {response['ErrorDetails'].get('Message')}"  # type: ignore
        )

    series = response.get("CompactData", {}).get("DataSet", {}).pop("Series", {})  # type: ignore

    if not series:
        raise KozmoAIError(f"No time series data found -> {response}")

    # If there is only one series, they ruturn a dict instead of a list.
    if series and isinstance(series, dict):
        series = [series]

    return series
