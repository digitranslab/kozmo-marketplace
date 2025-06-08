"""Views for the Currency Extension."""

from typing import TYPE_CHECKING, Any, Dict, Tuple

if TYPE_CHECKING:
    from kozmoai_charting.core.kozmoai_figure import (
        KozmoAIFigure,
    )


class CurrencyViews:
    """Currency Views."""

    @staticmethod
    def currency_price_historical(  # noqa: PLR0912
        **kwargs,
    ) -> Tuple["KozmoAIFigure", Dict[str, Any]]:
        """Currency Price Historical Chart."""
        # pylint: disable=import-outside-toplevel
        from kozmoai_charting.charts.price_historical import price_historical

        return price_historical(**kwargs)
