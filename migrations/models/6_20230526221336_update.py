from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "slots" ADD "supervisor_id" INT NOT NULL;
        ALTER TABLE "slots" ADD CONSTRAINT "fk_slots_supervis_f531c137" FOREIGN KEY ("supervisor_id") REFERENCES "supervisors" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "slots" DROP CONSTRAINT "fk_slots_supervis_f531c137";
        ALTER TABLE "slots" DROP COLUMN "supervisor_id";"""
