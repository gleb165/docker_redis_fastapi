from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY,ForeignKey, DateTime, TIMESTAMP)

from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+asyncpg://postgres:пдуи@localhost:5433/postgres'
engine = create_async_engine(DATABASE_URL)
metadata = MetaData()
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


performances = Table(
    'performances',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('price', Integer),
    Column('begin_data', DateTime),
    Column('begin_end', DateTime),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('description', String(250)),

)

places = Table(
    'places',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('size', Integer)
)

show = Table(
    'shows',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('price', Integer),
    Column('time_start', TIMESTAMP),
    Column('busy', Integer),
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('performances_id', Integer, ForeignKey('performances.id'))
)


database = Database(DATABASE_URL)
