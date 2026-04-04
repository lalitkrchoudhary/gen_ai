from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "FastAPI SQLite CRUD"
    api_v1_prefix: str = "/api/v1"

    database_url: str = "sqlite:///./app.db"
    sqlalchemy_echo: bool = False
    upload_dir: str = "./uploads"


settings = Settings()
