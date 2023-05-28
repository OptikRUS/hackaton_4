from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users_user_groups" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "group_id" INT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users_user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "users_user_groups" IS 'Группы пользователей';;
        CREATE TABLE IF NOT EXISTS "users_user_user_permissions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "permission_id" INT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users_user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "users_user_user_permissions" IS 'Права пользователей';;
        CREATE TABLE IF NOT EXISTS "meetings" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "start_url" VARCHAR(2048),
    "join_url" VARCHAR(2048),
    "status" VARCHAR(50) NOT NULL  DEFAULT 'not_approve',
    "is_approved" BOOL NOT NULL  DEFAULT False,
    "inspector_id" INT REFERENCES "users_user" ("id") ON DELETE SET NULL,
    "slot_id" INT REFERENCES "slots" ("id") ON DELETE SET NULL,
    "topic_id" INT NOT NULL REFERENCES "topics" ("id") ON DELETE CASCADE,
    "user_id" INT REFERENCES "users_user" ("id") ON DELETE SET NULL
);
COMMENT ON COLUMN "meetings"."start_url" IS 'URL начала встречи';
COMMENT ON COLUMN "meetings"."join_url" IS 'URL для присоединения';
COMMENT ON COLUMN "meetings"."status" IS 'Статус встречи';
COMMENT ON COLUMN "meetings"."is_approved" IS 'Подтверждена';
COMMENT ON TABLE "meetings" IS 'Запись на консультирование';;
        DROP TABLE IF EXISTS "appointments";
        DROP TABLE IF EXISTS "consultations";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users_user_groups";
        DROP TABLE IF EXISTS "users_user_user_permissions";
        DROP TABLE IF EXISTS "meetings";"""
