"""Test the auto_build feature."""

import importlib
import sys
from unittest.mock import patch

import pytest

# pylint: disable=redefined-outer-name, unused-import, import-outside-toplevel


@pytest.fixture(autouse=True)
def setup_mocks():
    """Set up mocks for the test."""
    with patch("kozmoai._PackageBuilder.auto_build") as mock_auto_build:
        mock_auto_build.return_value = None
        yield mock_auto_build


@pytest.fixture
def kozmoai_module(setup_mocks):
    """Reload the kozmoai module."""
    if "kozmoai" in sys.modules:
        importlib.reload(sys.modules["kozmoai"])
    else:
        pass
    return setup_mocks


@pytest.mark.integration
def test_autobuild_called(kozmoai_module):
    """Test that auto_build is called upon importing kozmoai."""
    kozmoai_module.assert_called_once()
