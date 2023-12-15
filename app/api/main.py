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


@app.post('/')
async def add(performances: PerformancesIn, db: AsyncSession = Depends(get_db)):
    await db_maneger.add_performance(performances, db)
    await db.commit()


@app.put('/{id}',response_model=list[PerformancesIn])
async def update(id: int, performances: PerformancesUpdate, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_performance(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="Not found")


    update_data = performances.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(perfo, key, value)

    await db.commit()
    await db.refresh(perfo)

    return perfo



@app.delete('/{id}')
async def delete(id: int, performances: PerformancesIn):
    perfo = await db_maneger.get_performance(id)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")
    return await db_maneger.delete_performance(id)
