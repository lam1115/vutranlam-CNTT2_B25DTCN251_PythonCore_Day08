from pydantic import BaseModel


class BookCreate(BaseModel):
    code: str
    title: str
    price: float
    pages: int


class BookResponse(BaseModel):
    id: int
    code: str
    title: str
    price: float
    pages: int

    class Config:
        from_attributes = True
