"""Test the router system module."""

from unittest.mock import patch

from kozmoai_core.api.router.system import get_system_model
from kozmoai_core.app.model.system_settings import SystemSettings


@patch("kozmoai_core.api.router.system.get_system_settings")
def test_get_system_model(mock_get_system_settings):
    """Test get system model."""
    mock_get_system_settings.return_value = SystemSettings()

    response = get_system_model(mock_get_system_settings)

    assert response
