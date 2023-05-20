from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "topics" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT
);
COMMENT ON COLUMN "topics"."name" IS 'Название темы консультирования';
COMMENT ON TABLE "topics" IS 'Тема консультирования';;
        CREATE TABLE IF NOT EXISTS "consultations" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT,
    "supervision_id" INT NOT NULL REFERENCES "supervisions" ("id") ON DELETE CASCADE,
    "supervisor_id" INT NOT NULL REFERENCES "supervisors" ("id") ON DELETE CASCADE,
    "topic_id" INT NOT NULL REFERENCES "topics" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "consultations"."name" IS 'Тема консультирования';
COMMENT ON TABLE "consultations" IS 'Консультация';;
"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "consultations";
        DROP TABLE IF EXISTS "topics";"""
