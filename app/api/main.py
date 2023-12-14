from fastapi import APIRouter, Header, HTTPException, Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db import AsyncSessionLocal
from app.api.models import PerformancesIn, PerformancesUpdate, PerformancesOut
from app.api import db_maneger

app = FastAPI()



async def get_db():
    async_db = AsyncSessionLocal()
    try:
        yield async_db
    finally:
        await async_db.close()


@app.get('/', response_model=list[PerformancesOut])
async def get_all_(db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_all_performance(db)


@app.post('/', status_code=201)
async def add(performances: PerformancesIn):
    per_id = await db_maneger.add_performance(performances)
    response = {
        'id': per_id,
        **performances.dict()
    }
    return response


@app.put('/{id}')
async def update(id: int, performances: PerformancesIn):
    perfo = await db_maneger.get_performance(id)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")
    update_data = performances.dict(exclude_unset=True)
    per_in_db = PerformancesIn(**perfo)

    updated_perfo = per_in_db.copy(update=update_data)

    return await db_maneger.update_movie(id, updated_perfo)


@app.delete('/{id}')
async def delete(id: int, performances: PerformancesIn):
    perfo = await db_maneger.get_performance(id)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")
    return await db_maneger.delete_performance(id)
