from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "supervisors" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT
);
        CREATE TABLE IF NOT EXISTS "supervisions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT,
    "supervisor_id" INT NOT NULL REFERENCES "supervisors" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "supervisions" IS 'Вид контроля (надзора)';;
COMMENT ON COLUMN "supervisions"."name" IS 'Вид контроля (надзора)';
COMMENT ON COLUMN "supervisors"."name" IS 'Наименование контрольного (надзорного) органа';
COMMENT ON TABLE "supervisors" IS 'Модель Контрольно-надзорного органа (КНО)';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "supervisions";
        DROP TABLE IF EXISTS "supervisors";"""
