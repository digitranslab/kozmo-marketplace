"""Test the CLI controller integration."""

from kozmoai_cli.controllers.cli_controller import (
    CLIController,
)


def test_parse_input_valid_commands():
    """Test parse_input method."""
    controller = CLIController()
    input_string = "exe --file test.kozmoai"
    expected_output = [
        "exe --file test.kozmoai"
    ]  # Adjust based on actual expected behavior
    assert controller.parse_input(input_string) == expected_output


def test_parse_input_invalid_commands():
    """Test parse_input method."""
    controller = CLIController()
    input_string = "nonexistentcommand args"
    expected_output = ["nonexistentcommand args"]
    actual_output = controller.parse_input(input_string)
    assert (
        actual_output == expected_output
    ), f"Expected {expected_output}, got {actual_output}"
