from pydantic import BaseModel


class Post(BaseModel):
    content: str
