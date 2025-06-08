"""KozmoAI Error."""

from typing import Optional, Union


class KozmoAIError(Exception):
    """KozmoAI Error."""

    def __init__(self, original: Optional[Union[str, Exception]] = None):
        """Initialize the KozmoAIError."""
        self.original = original
        super().__init__(str(original))
