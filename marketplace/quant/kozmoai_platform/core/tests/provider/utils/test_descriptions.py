"""Test the provider descriptions."""

from kozmoai_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


def test_query_descriptions():
    """Test the query descriptions."""
    assert QUERY_DESCRIPTIONS


def test_data_descriptions():
    """Test the data descriptions."""
    assert DATA_DESCRIPTIONS
