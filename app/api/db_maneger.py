from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models import (PerformancesOut, PerformancesIn, PerformancesUpdate)
from app.api.db import (performances, database)


async def add_performance(per: PerformancesIn, db: AsyncSession):
    return await db.execute(performances.insert().values(**per.dict()))


async def get_all_performance(db: AsyncSession):
    return (await db.execute(performances.select())).all()

    #return await database.fetch_all(query=performances.select())


async def get_performance(id: int, db: AsyncSession):
    return await db.execute(performances.select(performances.c.id == id))


async def delete_performance(id: int):
    query = performances.delete().where(performances.c.id == id)
    return await database.execute(query=query)


async def update_movie(id: int, per: PerformancesIn, db: AsyncSession):
    query = (
        performances
        .update()
        .where(performances.c.id == id)
        .values(**per)
    )
    return await db.execute(query=query)