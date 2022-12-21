import json
from typing import Union
from fastapi import APIRouter, Header, status, Depends
from app.src.exceptions.verify_comment import verify_comment
from app.src.utils.change_record import switch_vpn

router = APIRouter(
    prefix='/api',
    tags=['Action'],
    responses={200: {"Description": "Success"}},
)


@router.patch(
    '/action/{vpn_name}/{requester}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_comment)],
)
async def send_ticket(vpn_name: str, requester: str, comment: Union[str] = Header()):
    response = switch_vpn(vpn_name, requester, comment)
    return json.dumps(response, indent=4)
