"""Tests for root routes."""

# Standard library
from http import HTTPStatus

# Third party
from fastapi.testclient import TestClient
from httpx import Response

# First party
from app.main import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that the root endpoint returns the correct message.

    Returns:
        None: The test passes if the response is successful.
    """
    response: Response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello from hearth!"}
