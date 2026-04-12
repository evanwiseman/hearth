"""Tests for app module."""

# Standard library
from unittest.mock import patch

# First party
from app.main import main


def test_main_invokes_uvicorn() -> None:
    """``main`` should delegate to ``uvicorn.run`` with the ASGI app.

    The real ``uvicorn.run`` would block; we only assert the wiring.

    Returns:
        None: The test passes if ``uvicorn.run`` is invoked as expected.
    """
    with patch("app.main.uvicorn.run") as mock_run:
        main()
        mock_run.assert_called_once_with(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
        )
