"""Environment variables."""

import os
from pathlib import Path
from typing import Dict, Optional

import dotenv
from kozmoai_core.app.constants import KOZMOAI_DIRECTORY
from kozmoai_core.app.model.abstract.singleton import SingletonMeta


class Env(metaclass=SingletonMeta):
    """Environment variables."""

    _environ: Dict[str, str]

    def __init__(self) -> None:
        """Initialize the environment."""
        dotenv.load_dotenv(Path(KOZMOAI_DIRECTORY, ".env"))
        self._environ = os.environ.copy()

    @property
    def API_AUTH(self) -> bool:
        """API authentication: enables API endpoint authentication."""
        return self.str2bool(self._environ.get("KOZMOAI_API_AUTH", False))

    @property
    def API_USERNAME(self) -> Optional[str]:
        """API username: sets API username."""
        return self._environ.get("KOZMOAI_API_USERNAME", None)

    @property
    def API_PASSWORD(self) -> Optional[str]:
        """API password: sets API password."""
        return self._environ.get("KOZMOAI_API_PASSWORD", None)

    @property
    def API_AUTH_EXTENSION(self) -> Optional[str]:
        """Auth extension: specifies which authentication extension to use."""
        return self._environ.get("KOZMOAI_API_AUTH_EXTENSION", None)

    @property
    def AUTO_BUILD(self) -> bool:
        """Automatic build: enables automatic package build on import."""
        return self.str2bool(self._environ.get("KOZMOAI_AUTO_BUILD", True))

    @property
    def DEBUG_MODE(self) -> bool:
        """Debug mode: enables debug mode."""
        return self.str2bool(self._environ.get("KOZMOAI_DEBUG_MODE", False))

    @property
    def DEV_MODE(self) -> bool:
        """Dev mode: enables development mode."""
        return self.str2bool(self._environ.get("KOZMOAI_DEV_MODE", False))

    @property
    def HUB_BACKEND(self) -> str:
        """Hub backend: sets the backend for the KozmoAI Hub."""
        return self._environ.get("KOZMOAI_HUB_BACKEND", "https://payments.kozmoai.co")

    @staticmethod
    def str2bool(value) -> bool:
        """Match a value to its boolean correspondent."""
        if isinstance(value, bool):
            return value
        if value.lower() in {"false", "f", "0", "no", "n"}:
            return False
        if value.lower() in {"true", "t", "1", "yes", "y"}:
            return True
        raise ValueError(f"Failed to cast {value} to bool.")
