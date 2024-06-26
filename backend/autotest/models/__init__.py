from autotest.db.session import async_engine
from autotest.models.base import Base


async def init_db():
    """
    初始化数据库
    :return:
    """
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
