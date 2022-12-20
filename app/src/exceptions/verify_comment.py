from fastapi import HTTPException, Header
from typing import Union


def verify_comment(comment: Union[str, None] = Header(default=None)):
    if len(comment) <= 3:
        raise HTTPException(status_code=422, detail="Validation error")
