"""Main module."""

# Third party
import uvicorn
from fastapi import FastAPI

# First party
from app.api import api_router

app = FastAPI()
app.include_router(api_router)


def main() -> None:
    """Start the development server."""
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
