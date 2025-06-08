"""Test the UserSettings model."""

from kozmoai_core.app.model.credentials import Credentials
from kozmoai_core.app.model.defaults import Defaults
from kozmoai_core.app.model.preferences import Preferences
from kozmoai_core.app.model.profile import Profile
from kozmoai_core.app.model.user_settings import UserSettings


def test_user_settings():
    """Test the UserSettings model."""
    settings = UserSettings(
        credentials=Credentials(),
        profile=Profile(),
        preferences=Preferences(),
        defaults=Defaults(),
    )
    assert isinstance(settings, UserSettings)
