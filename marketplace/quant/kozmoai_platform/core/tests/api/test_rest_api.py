"""Test rest_api.py."""

from kozmoai_core.api.rest_api import app


def test_openapi():
    """Test openapi schema generation."""
    assert app.openapi()
