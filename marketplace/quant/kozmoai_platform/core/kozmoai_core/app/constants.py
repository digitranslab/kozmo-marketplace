"""Constants for the KozmoAI Platform."""

from pathlib import Path

HOME_DIRECTORY = Path.home()
KOZMOAI_DIRECTORY = Path(HOME_DIRECTORY, ".kozmoai_platform")
USER_SETTINGS_PATH = Path(KOZMOAI_DIRECTORY, "user_settings.json")
SYSTEM_SETTINGS_PATH = Path(KOZMOAI_DIRECTORY, "system_settings.json")
