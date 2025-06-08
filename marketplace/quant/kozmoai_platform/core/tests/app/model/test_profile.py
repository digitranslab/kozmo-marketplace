"""Test the profile class."""

from kozmoai_core.app.model.profile import Profile


def test_preferences():
    """Test the preferences class."""
    preferences = Profile()
    assert isinstance(preferences, Profile)
