from fastapi import HTTPException, Header
from typing import Union


def verify_token(x_auth_token: Union[str, None] = Header(default=None)):
    if x_auth_token == "" or x_auth_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if len(x_auth_token) < 65:
        raise HTTPException(status_code=422, detail="Validation error")
