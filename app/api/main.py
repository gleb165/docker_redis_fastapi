from fastapi import APIRouter, Header, HTTPException, Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.db_model import show
from app.api.db_model import AsyncSessionLocal
from app.api.db_maneger import update_performance, update_shows, update_places
from app.api.models import (PerformancesIn, PerformancesUpdate, PerformancesOut, placesIn, placesOut, placesUpdate, showsIn, showsOut, showUpdate)
from app.api import db_maneger, db_model

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


@app.get('/{id}', response_model=PerformancesIn)
async def get_one(id: int, db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_performance(id, db)


@app.post('/')
async def add(performances: PerformancesIn, db: AsyncSession = Depends(get_db)):
    db_per = db_model.Table()
    await db_maneger.add_performance(performances, db)
    await db.commit()
    for instance in db:
        await db.refresh(instance)

    return {'message': "performance add"}


@app.put('/{id}', response_model=PerformancesIn)
async def update(id: int, performances: PerformancesUpdate, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_performance(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="Not found")

    await update_performance(id, performances.dict(exclude_unset=True), db)

    await db.commit()
    return await db_maneger.get_performance(id, db)





@app.delete('/{id}')
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_performance(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")

    await db_maneger.delete_performance(id, db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return {'message': 'performance delete'}


@app.get('/places/', response_model=list[placesOut])
async def get_all_(db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_all_places(db)


@app.post('/places/')
async def add(places: placesIn, db: AsyncSession = Depends(get_db)):
    await db_maneger.add_places(places, db)
    await db.commit()
    for instance in db:
        await db.refresh(instance)

    return {'message': "performance add"}


@app.get('/places/{place_id}', response_model=placesIn)
async def get_one(place_id: int, db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_places(place_id, db)


@app.delete('/places/{place_id}')
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_places(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")

    await db_maneger.delete_places(id, db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return {'message': 'places delete'}


@app.put('/places/{place_id}', response_model=placesIn)
async def update(id: int, pla: placesUpdate, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_places(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="Not found")

    await update_places(id, pla.dict(exclude_unset=True), db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return await db_maneger.get_places(id, db)


@app.get('/show/', response_model=list[showsOut])
async def get_all_(db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_all_shows(db)


@app.post('/show/')
async def add(sh: showsIn, db: AsyncSession = Depends(get_db)):
    await db_maneger.add_shows(sh, db)
    await db.commit()
    for instance in db:
        await db.refresh(instance)

    return {'message': "performance add"}


@app.get('/show/{show_id}', response_model=showsIn)
async def get_one(show_id: int, db: AsyncSession = Depends(get_db)):
    return await db_maneger.get_shows(show_id, db)


@app.delete('/show/{show_id}')
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_shows(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")

    await db_maneger.delete_shows(id, db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return {'message': 'places delete'}


@app.put('/show/{show_id}', response_model=showsIn)
async def update(id: int, pla: showUpdate, db: AsyncSession = Depends(get_db)):
    perfo = await db_maneger.get_shows(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="Not found")

    await update_shows(id, pla.dict(exclude_unset=True), db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return await db_maneger.get_shows(id, db)





@app.get("/subtract_tickets/{num_to_subtract}/{id}")
async def subtract_tickets(num_to_subtract: int, id: int, db: AsyncSession = Depends(get_db)):
    show_in_row = (await db.execute(show.select().with_only_columns([show.c.busy]).where(show.c.id == id))).all()
    current_busy = show_in_row[0]
    current_busy = current_busy['busy']

    if current_busy >= num_to_subtract:
        new_busy = current_busy - num_to_subtract
        await db.execute(show.update().values(busy=new_busy).where(show.c.id == id))
        await db.commit()
        return {"message": f"Subtracted {num_to_subtract} tickets. Remaining tickets: {new_busy}"}
    else:
        raise HTTPException(status_code=400, detail="Not enough tickets available.")