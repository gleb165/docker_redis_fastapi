from pydantic import BaseModel


class Performances(BaseModel):
    name: str
    price: int
    plot: str
    genres: list
    description: str | None = None
