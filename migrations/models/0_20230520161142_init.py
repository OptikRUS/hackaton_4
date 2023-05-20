from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "password" VARCHAR(128),
    "is_active" BOOL NOT NULL  DEFAULT True,
    "role" VARCHAR(9) NOT NULL  DEFAULT 'client'
);
COMMENT ON TABLE "users" IS 'Модель пользователя';
CREATE TABLE IF NOT EXISTS "gis_services" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(250) NOT NULL UNIQUE,
    "description" TEXT
);
COMMENT ON TABLE "gis_services" IS 'Модель сервиса ГИС';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
