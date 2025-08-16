from typing import AsyncIterator
from ..db.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncIterator[AsyncSession]:
    async with get_async_session() as session:
        yield session
