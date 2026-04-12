"""Root route."""

# Third party
from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
async def read_root() -> dict[str, str]:
    """Read the root.

    Returns:
        dict[str, str]: The message.
    """
    return {"message": "Hello from hearth!"}
