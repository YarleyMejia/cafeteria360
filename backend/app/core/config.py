import json
from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CafeterIA 360 API"
    env: str = "development"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    cors_origins: Annotated[list[str], NoDecode] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, list):
            return value
        if not isinstance(value, str):
            return []

        raw = value.strip()
        if not raw:
            return []

        if raw.startswith("["):
            parsed = json.loads(raw)
            return [item.strip() for item in parsed if isinstance(item, str) and item.strip()]

        return [item.strip() for item in raw.split(",") if item.strip()]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
