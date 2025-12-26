from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str
    pages: int
    price: float


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
