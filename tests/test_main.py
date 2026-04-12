"""Tests for main module."""

# Third party
import pytest

# First party
from src.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that main runs without error.

    Args:
        capsys: Pytest fixture to capture stdout and stderr.
    """
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from hearth!\n"
