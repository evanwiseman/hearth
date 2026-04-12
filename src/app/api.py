"""Assembled API routes."""

# Third party
from fastapi import APIRouter

# First party
from app.routes.root import router as root_router

api_router = APIRouter()
api_router.include_router(root_router)
