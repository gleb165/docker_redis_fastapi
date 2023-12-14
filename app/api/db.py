from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

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
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('description', String(250))
)


database = Database(DATABASE_URL)
