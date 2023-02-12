from pydantic import BaseModel


class Book(BaseModel):
    author: str
    id: int
    isElectronicBook: bool
    name: str
    year: int
