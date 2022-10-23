from typing import Union
from fastapi import APIRouter, Header, status, Depends
from app.src.utils.get_attributes import get_all_records
from app.src.utils.verify_token import verify_token

router = APIRouter(
    prefix='/api',
    tags=['Get all records'],
    responses={401: {"description": "Unauthorized"}},
)


@router.get(
    '/get-records/{vpn_name}',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)],
)
async def get_records(vpn_name: str, x_auth_token: Union[str, None] = Header(default=None)):
    response_body = get_all_records(vpn_name, x_auth_token)
    return response_body
