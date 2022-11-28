import json
from typing import Union
from fastapi import APIRouter, Header, status, Depends
from app.src.utils.mgmt_record import update_record_alternate, update_record_location
from app.src.exceptions.verify_token import verify_token

router = APIRouter(
    prefix='/api',
    tags=['Action'],
    responses={401: {"description": "Unauthorized"}},
)


@router.patch(
    '/action/{vpn_name}/{requester}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_token)],
)
async def send_ticket(vpn_name: str, requester: str, x_auth_token: Union[str] = Header()):
    response_body = {
        'alternate': update_record_alternate(vpn_name, requester, x_auth_token),
        'location': update_record_location(vpn_name, requester, x_auth_token)
    }
    return json.dumps(response_body, indent=4)
