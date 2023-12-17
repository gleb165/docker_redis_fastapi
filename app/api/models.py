from pydantic import BaseModel
from datetime import datetime


# performances = Table(
#     'performances',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(50)),
#     Column('price', Integer),
#     Column('begin_data', DateTime),
#     Column('begin_end',DateTime),
#     Column('plot', String(250)),
#     Column('genres', ARRAY(String)),
#     Column('description', String(250)),
#
# )
class PerformancesIn(BaseModel):
    name: str
    price: int
    begin_data: datetime
    begin_end: datetime
    plot: str
    genres: list
    description: str


class PerformancesOut(PerformancesIn):
    id: int


class PerformancesUpdate(PerformancesIn):
    name: str | None = None
    price: int | None = None
    begin_data: datetime | None = None
    begin_end: datetime | None = None
    plot: str | None = None
    genres: list | None = None
    description: str | None = None

    # places = Table(
    #     'places',
    #     metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String(50)),
    #     Column('size'), Integer)


class placesIn(BaseModel):
    name: str
    size: int


class placesOut(placesIn):
    id: int


class placesUpdate(placesIn):
    name: str | None = None
    size: int | None = None

    # show = Table(
    #     'shows',
    #     metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('price', Integer),
    #     Column('time_start', TIMESTAMP),
    #     Column('busy', Integer),
    #     Column('place_id', Integer, ForeignKey('places.id')),
    #     Column('performances_id', Integer, ForeignKey('performances.id'))
    # )


class showsIn(BaseModel):
    price: int
    time_start: datetime
    busy: int
    place_id: int
    performances_id: int


class showsOut(showsIn):
    id: int


class showUpdate(showsIn):
    price: int | None = None
    time_start: datetime | None = None
    busy: int | None = None

