from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME TO "users_user";
        ALTER TABLE "users_user" ADD "last_name" VARCHAR(250);
        ALTER TABLE "users_user" ADD "is_superuser" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "users_user" ADD "first_name" VARCHAR(250);
        ALTER TABLE "users_user" ADD "email" VARCHAR(256);
        ALTER TABLE "users_user" ADD "last_login" TIMESTAMPTZ;
        ALTER TABLE "users_user" ADD "is_staff" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "users_user" ADD "date_joined" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users_user" RENAME TO "users";
        ALTER TABLE "users_user" DROP COLUMN "last_name";
        ALTER TABLE "users_user" DROP COLUMN "is_superuser";
        ALTER TABLE "users_user" DROP COLUMN "first_name";
        ALTER TABLE "users_user" DROP COLUMN "email";
        ALTER TABLE "users_user" DROP COLUMN "last_login";
        ALTER TABLE "users_user" DROP COLUMN "is_staff";
        ALTER TABLE "users_user" DROP COLUMN "date_joined";"""
