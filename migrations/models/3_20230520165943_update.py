from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "regulation_types" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100)
);
COMMENT ON COLUMN "regulation_types"."name" IS 'Название типа нормативно-правового акта';
COMMENT ON TABLE "regulation_types" IS 'Тип нормативно-правового акта';;
        CREATE TABLE IF NOT EXISTS "regulations" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT,
    "created_at" DATE NOT NULL,
    "publication_date" DATE NOT NULL,
    "regulation_type_id" INT REFERENCES "regulation_types" ("id") ON DELETE SET NULL,
    "supervision_id" INT REFERENCES "supervisions" ("id") ON DELETE SET NULL,
    "supervisor_id" INT REFERENCES "supervisors" ("id") ON DELETE SET NULL
);
COMMENT ON COLUMN "regulations"."name" IS 'Наименование документа';
COMMENT ON COLUMN "regulations"."created_at" IS 'Дата документа';
COMMENT ON COLUMN "regulations"."publication_date" IS 'Дата публикации';
COMMENT ON TABLE "regulations" IS 'Нормативно-правовой акт';;
"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "regulations";
        DROP TABLE IF EXISTS "regulation_types";"""
