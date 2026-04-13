"""Hearth application settings module."""

# Third party
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Hearth application settings."""

    app_env: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="_",
        extra="allow",
    )


settings = Settings()
