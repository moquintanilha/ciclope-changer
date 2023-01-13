from fastapi import APIRouter

router = APIRouter(
    tags=['Health Check'],
    responses={500: {"description": "Internal server error"}},
)


@router.get('/ping')
async def health_check():
    try:
        return 'pong'
    except Exception as e:
        raise e
