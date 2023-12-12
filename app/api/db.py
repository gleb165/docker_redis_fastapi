from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:пдуи@localhost/postgres'
engine = create_engine(DATABASE_URL)
metadata = MetaData()

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
