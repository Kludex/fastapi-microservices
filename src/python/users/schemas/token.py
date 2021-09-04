from typing import Literal, Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"]


class TokenPayload(BaseModel):
    user_id: Optional[int]
