from datetime import timedelta
from os import environ as env
from pathlib import Path

from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).parent.parent.parent


class DatabaseConfig(BaseModel):
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    login: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    database: str = Field(alias="POSTGRES_DB")

    def get_connection_url(self) -> str:
        return f"postgresql+asyncpg://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}"


class JWTAuthConfig(BaseModel):
    algorithm: str = "RS256"
    private_key: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key: Path = BASE_DIR / "certs" / "jwt-public.pem"
    access_expire_minutes: timedelta = Field(default=timedelta(minutes=10))
    refresh_expire_days: timedelta = Field(default=timedelta(days=10))


class Config(BaseModel):
    auth_jwt: JWTAuthConfig = Field(default_factory=lambda: JWTAuthConfig())
    postgres: DatabaseConfig = Field(
        default_factory=lambda: DatabaseConfig(**env),
    )
