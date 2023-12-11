from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from app.api.models import Performances

per = APIRouter()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


@per.get('/performance')
async def get_performance(performances: Performances) -> Performances:
    return fake_movie_db


@per.post('/performance', status_code=201)
async def post_performance(performances: Performances):
    per = performances.dict()
    fake_movie_db.append(per)
    return {'id': len(fake_movie_db) - 1}


@per.put('/performance/{id}')
async def update_performance(id: int, performances: Performances):
    len_performances = len(fake_movie_db)
    if 0 <= id < len_performances:
        fake_movie_db[id] = performances
        return fake_movie_db
    raise HTTPException(status_code=404, detail="Performance with given id not found")


@per.delete('/performance/{id}')
async def delete_performance(id: int, performances: Performances):
    len_performances = len(fake_movie_db)
    if 0 <= id < len_performances:
        return fake_movie_db.remove(fake_movie_db[id])
