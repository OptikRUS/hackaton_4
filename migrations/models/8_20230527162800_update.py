from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" ADD "join_url" VARCHAR(2048) NOT NULL;
        ALTER TABLE "appointments" ADD "status" VARCHAR(50) NOT NULL;
        ALTER TABLE "appointments" ADD "topic_id" INT NOT NULL;
        ALTER TABLE "appointments" ADD "start_url" VARCHAR(2048) NOT NULL;
        ALTER TABLE "appointments" ADD CONSTRAINT "fk_appointm_topics_a7c3d025" FOREIGN KEY ("topic_id") REFERENCES "topics" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" DROP CONSTRAINT "fk_appointm_topics_a7c3d025";
        ALTER TABLE "appointments" DROP COLUMN "join_url";
        ALTER TABLE "appointments" DROP COLUMN "status";
        ALTER TABLE "appointments" DROP COLUMN "topic_id";
        ALTER TABLE "appointments" DROP COLUMN "start_url";"""
