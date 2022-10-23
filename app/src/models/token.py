from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    client_id: Union[str, None] = None
    secret: str
