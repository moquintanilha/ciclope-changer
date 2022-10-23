from typing import Optional

from pydantic import BaseModel


class VPNAttributes(BaseModel):
    id: Optional[str] = None
    ip: Optional[str] = None
    vpn_status: Optional[bool] = None

