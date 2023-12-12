from fastapi import APIRouter, Header, HTTPException
from app.api.models import PerformancesIn, PerformancesUpdate, PerformancesOut
from app.api import db_maneger


per = APIRouter()


@per.get('/', response_model=PerformancesOut)
async def get_all_():
    return db_maneger.get_all_performance()


@per.post('/', status_code=201)
async def add(performances: PerformancesIn):
    per_id = await db_maneger.add_performance(performances)
    response = {
        'id': per_id,
        **performances.dict()
    }
    return response


@per.put('/{id}')
async def update(id: int, performances: PerformancesIn):
    perfo = await db_maneger.get_performance(id)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")
    update_data = performances.dict(exclude_unset=True)
    per_in_db = PerformancesIn(**perfo)

    updated_perfo = per_in_db.copy(update=update_data)

    return await db_maneger.update_movie(id, updated_perfo)


@per.delete('/{id}')
async def delete(id: int, performances: PerformancesIn):
    perfo = await db_maneger.get_performance(id)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")
    return await db_maneger.delete_performance(id)
