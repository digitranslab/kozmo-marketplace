"""Test the preferences class."""

from kozmoai_core.app.model.preferences import Preferences


def test_preferences():
    """Test the preferences class."""
    preferences = Preferences()
    assert isinstance(preferences, Preferences)
