from app.api.models import (PerformancesOut, PerformancesIn, PerformancesUpdate)
from app.api.db import (performances, database)


async def add_performance(per: PerformancesIn):
    query = performances.insert().values(**per.dict())
    return await database.execute(query=query)


async def get_all_performance():
    return await database.fetch_all(query=performances.select())


async def get_performance(id: int):
    query = performances.select(performances.c.id == id)
    return await database.fetch_one(query)


async def delete_performance(id: int):
    query = performances.delete().where(performances.c.id == id)
    return await database.execute(query=query)


async def update_movie(id: int, per: PerformancesIn):
    query = (
        performances
        .update()
        .where(performances.c.id == id)
        .values(**per.dict())
    )
    return await database.execute(query=query)