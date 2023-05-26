from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" DROP COLUMN "supervisor_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "appointments" ADD "supervisor_id" INT;
        ALTER TABLE "appointments" ADD CONSTRAINT "fk_appointm_supervis_79e2fc42" FOREIGN KEY ("supervisor_id") REFERENCES "supervisors" ("id") ON DELETE SET NULL;"""
