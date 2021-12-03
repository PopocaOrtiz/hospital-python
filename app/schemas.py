from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
