from pydantic import BaseSettings, Field, validator


class SiteSettings(BaseSettings):
    host: str = Field("127.0.0.1", env="SITE_HOST")
    port: int = Field(8000, env="SITE_PORT")
    loop: str = Field("asyncio")
    log_level: str = Field("info", env="SITE_LOG_LEVEL")
    reload_delay: float = Field(0.25, env="SITE_RELOAD_DELAY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ApplicationSettings(BaseSettings):
    title: str = Field("Fastapi with tortoise ORM template")
    description = Field("Шаблон приложения на tortoise ORM")
    debug: bool = Field(True, env="DEBUG")
    version: str = Field("0.1.0", env="APP_VERSION")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseCredentials(BaseSettings):
    user: str = Field("postgres", env="DATABASE_USER")
    password: str = Field("postgres", env="DATABASE_PASSWORD")
    port: str = Field("5432", env="DATABASE_PORT")
    db_name: str = Field("db_app", env="DATABASE_NAME")
    host: str = Field("localhost", env="DATABASE_HOST")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseConnections(BaseSettings):
    default: str = Field("postgres://{user}:{password}@{host}:{port}/{db_name}")

    @validator("default", pre=True)
    def generate_db_url(cls, db_url):
        return db_url.format(**DataBaseCredentials().dict())


class DataBaseModels(BaseSettings):
    models: list[str] = Field(
        [
            ...
        ]
    )


class DataBaseSettings(BaseSettings):
    connections: dict = Field(DataBaseConnections())
    apps: dict = Field(dict(models=DataBaseModels()))


class TortoiseSettings(BaseSettings):
    generate_schemas: bool = Field(True, env="TORTOISE_GENERATE_SCHEMAS")
    add_exception_handlers: bool = Field(True, env="DATABASE_EXCEPTION_HANDLERS")