from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" ADD "is_approved" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "appointments" ADD "inspector_id" INT;
        ALTER TABLE "appointments" ALTER COLUMN "status" SET DEFAULT 'not_approve';
        ALTER TABLE "appointments" ALTER COLUMN "join_url" DROP NOT NULL;
        ALTER TABLE "appointments" ALTER COLUMN "start_url" DROP NOT NULL;
        ALTER TABLE "appointments" ADD CONSTRAINT "fk_appointm_users_us_5de0a083" FOREIGN KEY ("inspector_id") REFERENCES "users_user" ("id") ON DELETE SET NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" DROP CONSTRAINT "fk_appointm_users_us_5de0a083";
        ALTER TABLE "appointments" DROP COLUMN "is_approved";
        ALTER TABLE "appointments" DROP COLUMN "inspector_id";
        ALTER TABLE "appointments" ALTER COLUMN "status" DROP DEFAULT;
        ALTER TABLE "appointments" ALTER COLUMN "join_url" SET NOT NULL;
        ALTER TABLE "appointments" ALTER COLUMN "start_url" SET NOT NULL;"""
