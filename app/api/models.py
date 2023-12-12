from pydantic import BaseModel


class PerformancesIn(BaseModel):
    name: str
    price: int
    plot: str
    genres: list
    description: str


class PerformancesOut(PerformancesIn):
    id: int


class PerformancesUpdate(PerformancesIn):
    name: str | None = None
    price: int | None = None
    plot: str | None = None
    genres: list | None = None
    description: str | None = None
