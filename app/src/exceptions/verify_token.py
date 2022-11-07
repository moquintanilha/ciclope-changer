from fastapi import HTTPException, Header
from typing import Union


def verify_token(x_auth_token: Union[str, None] = Header(default=None)):
    if len(x_auth_token) == "":
        raise HTTPException(status_code=422, detail="Validation error")
