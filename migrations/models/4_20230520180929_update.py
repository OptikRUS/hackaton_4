from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "role" TYPE VARCHAR(10) USING "role"::VARCHAR(10);
        CREATE TABLE IF NOT EXISTS "slots" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "slot_date" DATE NOT NULL,
    "slot_time" TIMETZ NOT NULL,
    "is_open" BOOL NOT NULL  DEFAULT True
);
        CREATE TABLE IF NOT EXISTS "appointments" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "slot_id" INT REFERENCES "slots" ("id") ON DELETE SET NULL,
    "supervisor_id" INT REFERENCES "supervisors" ("id") ON DELETE SET NULL,
    "user_id" INT REFERENCES "users" ("id") ON DELETE SET NULL
);
COMMENT ON TABLE "appointments" IS 'Запись на консультирование';;
COMMENT ON COLUMN "slots"."slot_date" IS 'Дата слота';
COMMENT ON COLUMN "slots"."slot_time" IS 'Время слота';
COMMENT ON COLUMN "slots"."is_open" IS 'Доступность слота';
COMMENT ON TABLE "slots" IS 'Слот записи на консультирование';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "role" TYPE VARCHAR(9) USING "role"::VARCHAR(9);
        DROP TABLE IF EXISTS "appointments";
        DROP TABLE IF EXISTS "slots";"""
