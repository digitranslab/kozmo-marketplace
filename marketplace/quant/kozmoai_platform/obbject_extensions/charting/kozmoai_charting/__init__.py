"""KozmoAI OBBject extension for charting."""

import warnings

from kozmoai_core.app.model.extension import Extension

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="kozmoai_core.app.model.extension",
)


def get_charting_module():
    """Get the Charting module."""
    # pylint: disable=import-outside-toplevel
    import importlib

    _Charting = importlib.import_module("kozmoai_charting.charting").Charting
    return _Charting


ext = Extension(name="charting", description="Create custom charts from OBBject data.")

Charting = ext.obbject_accessor(get_charting_module())
