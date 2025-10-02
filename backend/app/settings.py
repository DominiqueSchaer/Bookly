from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


NEON_DATABASE_URL = (
    "postgresql+asyncpg://neondb_owner:"
    "npg_WDZ0d4mhUBPt"
    "@ep-polished-mouse-agnqozc5-pooler.c-2.eu-central-1.aws.neon.tech/neondb"
    "?ssl=require"
)


class Settings(BaseSettings):
    app_name: str = Field(default="Bookly API", alias="APP_NAME")
    database_url: str = Field(default=NEON_DATABASE_URL, alias="DATABASE_URL")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


settings = get_settings()
