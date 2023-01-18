from pydantic import BaseModel


class Like(BaseModel):
    user_id: int
    post_id: int
