"""Tests for the SystemSettings class."""

import os
from pathlib import Path

import pytest
from kozmoai_core.app.model.system_settings import SystemSettings
from pydantic import BaseModel, ConfigDict


class MockSystemSettings(BaseModel):
    """Mock SystemSettings."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


def test_system_settings():
    """Test the SystemSettings class."""
    sys = SystemSettings()
    assert isinstance(sys, SystemSettings)


def test_create_kozmoai_directory_directory_and_files_not_exist(tmpdir):
    """Test the create_kozmoai_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "kozmoai_directory": str(tmpdir.join("kozmoai")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Act
    SystemSettings.create_kozmoai_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.kozmoai_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


def test_create_kozmoai_directory_directory_exists_user_settings_missing(tmpdir):
    """Test the create_kozmoai_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "kozmoai_directory": str(tmpdir.join("kozmoai")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Create the kozmoai directory
    Path(values.kozmoai_directory).mkdir(parents=True, exist_ok=True)  # type: ignore[attr-defined]

    # Act
    SystemSettings.create_kozmoai_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.kozmoai_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


def test_create_kozmoai_directory_directory_exists_system_settings_missing(tmpdir):
    """Test the create_kozmoai_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "kozmoai_directory": str(tmpdir.join("kozmoai")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Create the kozmoai directory
    Path(values.kozmoai_directory).mkdir(parents=True, exist_ok=True)  # type: ignore[attr-defined]

    # Create the user_settings.json file
    with open(values.user_settings_path, "w") as f:  # type: ignore[attr-defined]
        f.write("{}")

    # Act
    SystemSettings.create_kozmoai_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.kozmoai_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "values, expected_handlers",
    [
        # Test case: test_mode is True, logging_suppress is True
        (
            {
                "debug_mode": True,
                "test_mode": True,
                "logging_suppress": True,
                "log_collect": True,
                "logging_handlers": [],
            },
            [],
        ),
        # Test case: test_mode is False, logging_suppress is True
        (
            {
                "debug_mode": False,
                "test_mode": False,
                "logging_suppress": True,
                "log_collect": True,
                "logging_handlers": [],
            },
            [],
        ),
        # Test case: test_mode is False, logging_suppress is False, log_collect is True,
        # and "posthog" handler is not present in logging_handlers
        (
            {
                "debug_mode": False,
                "test_mode": False,
                "logging_suppress": False,
                "log_collect": True,
                "logging_handlers": ["file", "console"],
            },
            ["file", "console", "posthog"],
        ),
        # Test case: test_mode is False, logging_suppress is False, log_collect is True,
        # and "posthog" handler is already present in logging_handlers
        (
            {
                "debug_mode": False,
                "test_mode": False,
                "logging_suppress": False,
                "log_collect": True,
                "logging_handlers": ["file", "console", "posthog"],
            },
            ["file", "console", "posthog"],
        ),
    ],
)
def test_validate_posthog_handler(values, expected_handlers):
    """Test the validate_posthog_handler method."""
    values = MockSystemSettings(**values)
    # Act
    result = SystemSettings.validate_posthog_handler(values)  # type: ignore[operator]

    # Assert
    assert result.logging_handlers == expected_handlers


@pytest.mark.parametrize(
    "handlers, valid",
    [
        # Test case: Valid handlers
        (["stdout", "file", "noop"], True),
        # Test case: Invalid handler
        (["stdout", "invalid_handler", "file"], False),
        # Test case: Empty list of handlers
        ([], True),
        # Test case: Repeated valid handlers
        (["stdout", "stderr", "stdout", "noop", "stderr"], True),
    ],
)
def test_validate_logging_handlers(handlers, valid):
    """Test the validate_logging_handlers method."""
    # Act and Assert
    if valid:
        assert SystemSettings.validate_logging_handlers(handlers) == handlers  # type: ignore[call-arg]
    else:
        with pytest.raises(ValueError, match="Invalid logging handler"):
            SystemSettings.validate_logging_handlers(handlers)  # type: ignore[call-arg]
