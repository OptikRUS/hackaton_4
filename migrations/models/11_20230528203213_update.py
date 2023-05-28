from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users_user" ADD "supervisor_id" INT;
        ALTER TABLE "users_user" ADD CONSTRAINT "fk_users_us_supervis_5dc34ca3" FOREIGN KEY ("supervisor_id") REFERENCES "supervisors" ("id") ON DELETE SET NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users_user" DROP CONSTRAINT "fk_users_us_supervis_5dc34ca3";
        ALTER TABLE "users_user" DROP COLUMN "supervisor_id";"""
