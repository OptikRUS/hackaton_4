from pydantic import BaseSettings, Field, validator


class AdvancedSettings(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SiteSettings(AdvancedSettings):
    host: str = Field("127.0.0.1", env="SITE_HOST")
    port: int = Field(8000)
    loop: str = Field("asyncio")
    log_level: str = Field("info", env="SITE_LOG_LEVEL")
    reload_delay: float = Field(0.25, env="SITE_RELOAD_DELAY")


class ApplicationSettings(AdvancedSettings):
    title: str = Field('Хакатон "Лидеры цифровой информации"')
    description: str = Field("Мобильное приложение для прохождения предпринимателями проверок контрольных органов")
    debug: bool = Field(True, env="DEBUG")
    version: str = Field("0.1.0", env="APP_VERSION")


class DataBaseCredentials(AdvancedSettings):
    # postgres
    user: str = Field("postgres", env="DATABASE_USER")
    password: str = Field("postgres", env="DATABASE_PASSWORD")
    port: str = Field("5432", env="DATABASE_PORT")
    db_name: str = Field("db_app", env="DATABASE_NAME")
    host: str = Field("localhost", env="DATABASE_HOST")


class DataBaseConnections(AdvancedSettings):
    default: str = Field("postgres://{user}:{password}@{host}:{port}/{db_name}")

    @validator("default", pre=True)
    def generate_db_url(cls, db_url):
        return db_url.format(**DataBaseCredentials().dict())


class DataBaseModels(AdvancedSettings):
    models: list[str] = Field(
        [
            "aerich.models",
            "src.users.repos",
            "src.gis.repos",
            "src.counseling.repos",
            "src.meetings.repos",
        ]
    )


class DataBaseSettings(AdvancedSettings):
    connections: dict = Field(DataBaseConnections())
    apps: dict = Field(dict(models=DataBaseModels()))


class TortoiseSettings(AdvancedSettings):
    generate_schemas: bool = Field(True, env="TORTOISE_GENERATE_SCHEMAS")
    add_exception_handlers: bool = Field(True, env="DATABASE_EXCEPTION_HANDLERS")


class AuthSettings(AdvancedSettings):
    type: str = Field("Bearer")
    password_time: int = Field(3)
    algorithm: str = Field("HS256")
    expires: int = Field(60*60, env="TOKEN_EXPIRES")
    hasher_deprecated: str = Field("auto")
    hasher_schemes: list[str] = Field(["bcrypt"])
    token_url: str = Field("users/login")

    secret_key: str = Field("secret_key", env="AUTH_SECRET_KEY")


class CORSSettings(AdvancedSettings):
    allow_credentials: bool = Field(True)
    allow_methods: list[str] = Field(["*"])
    allow_headers: list[str] = Field(["*", "Authorization"])
    allow_origins: list[str] = Field(["*"], env="CORS_ORIGINS")


class SuperUsersSettings(AdvancedSettings):
    superusers: list[str] = Field(["admin"], env="SUPER_USERS")


class ZoomSettings(AdvancedSettings):
    base_url: str = Field("https://api.zoom.us/v2", env="ZOOM_URL")
    api_key: str = Field("api_key", env="ZOOM_API_KEY")
    api_secret: str = Field("api_key", env="ZOOM_API_SECRET")
