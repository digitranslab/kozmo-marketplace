"""Test the CLI module."""

from unittest.mock import patch

from kozmoai_cli.cli import main


@patch("kozmoai_cli.config.setup.bootstrap")
@patch("kozmoai_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["kozmoai", "--dev", "--debug"])
def test_main_with_dev_and_debug(mock_launch, mock_bootstrap):
    """Test the main function with dev and debug flags."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(True, True)


@patch("kozmoai_cli.config.setup.bootstrap")
@patch("kozmoai_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["kozmoai"])
def test_main_without_arguments(mock_launch, mock_bootstrap):
    """Test the main function without arguments."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(False, False)


@patch("kozmoai_cli.config.setup.bootstrap")
@patch("kozmoai_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["kozmoai", "--dev"])
def test_main_with_dev_only(mock_launch, mock_bootstrap):
    """Test the main function with dev flag only."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(True, False)


@patch("kozmoai_cli.config.setup.bootstrap")
@patch("kozmoai_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["kozmoai", "--debug"])
def test_main_with_debug_only(mock_launch, mock_bootstrap):
    """Test the main function with debug flag only."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(False, True)
