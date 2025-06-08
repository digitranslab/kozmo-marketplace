"""Test the HubUserSettings class."""

from kozmoai_core.app.model.hub.hub_user_settings import HubUserSettings


def test_hub_user_settings():
    """Test the HubUserSettings class."""
    hub_settings = HubUserSettings()

    assert isinstance(hub_settings, HubUserSettings)
