from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models import (PerformancesOut, PerformancesIn, PerformancesUpdate, placesIn,showsIn)
from app.api.db_model import (performances, database, places, show)

# model for performance


async def add_performance(per: PerformancesIn, db: AsyncSession):
    return await db.execute(performances.insert().values(**per.dict()))


async def get_all_performance(db: AsyncSession):
    return (await db.execute(performances.select())).all()

    #return await database.fetch_all(query=performances.select())


async def get_performance(id: int, db: AsyncSession):
    return (await db.execute(performances.select(performances.c.id == id))).fetchone()


async def delete_performance(id: int, db: AsyncSession):
    query = performances.delete().where(performances.c.id == id)
    return await db.execute(query)


async def update_performance(id: int, per: PerformancesIn, db: AsyncSession):

    return await db.execute(performances
                            .update()
                            .where(performances.c.id == id)
                            .values(**per))

# model for places
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
async def add_places(pla: placesIn , db: AsyncSession):
    return await db.execute(places.insert().values(**pla.dict()))


async def get_all_places(db: AsyncSession):
    return (await db.execute(places.select())).all()

    #return await database.fetch_all(query=performances.select())






async def get_places(id: int, db: AsyncSession):
    return (await db.execute(places.select(places.c.id == id))).fetchone()


async def delete_places(id: int, db: AsyncSession):
    query = places.delete().where(places.c.id == id)
    return await db.execute(query)


async def update_places(id: int, pla: placesIn, db: AsyncSession):

    return await db.execute(places
                            .update()
                            .where(places.c.id == id)
                            .values(**pla))


# model for shows
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

async def add_shows(pla: showsIn , db: AsyncSession):
    return await db.execute(show.insert().values(**pla.dict()))


async def get_all_shows(db: AsyncSession):
    return (await db.execute(show.select())).all()

    #return await database.fetch_all(query=performances.select())


async def get_shows(id: int, db: AsyncSession):
    return (await db.execute(show.select(show.c.id == id))).fetchone()


async def delete_shows(id: int, db: AsyncSession):
    query = show.delete().where(show.c.id == id)
    return await db.execute(query)


async def update_shows(id: int, sh: showsIn, db: AsyncSession):

    return await db.execute(show
                            .update()
                            .where(show.c.id == id)
                            .values(**sh))


# class showsIn(BaseModel):
#     price: int
#     time_start: datetime
#     busy: int
#     place_id: int
#     performances_id: int