"""User settings model."""

from kozmoai_core.app.model.abstract.tagged import Tagged
from kozmoai_core.app.model.credentials import Credentials
from kozmoai_core.app.model.defaults import Defaults
from kozmoai_core.app.model.preferences import Preferences
from kozmoai_core.app.model.profile import Profile
from pydantic import Field


class UserSettings(Tagged):
    """User settings."""

    profile: Profile = Field(default_factory=Profile)
    credentials: Credentials = Field(default_factory=Credentials)
    preferences: Preferences = Field(default_factory=Preferences)
    defaults: Defaults = Field(default_factory=Defaults)

    def __repr__(self) -> str:
        """Human readable representation of the object."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
