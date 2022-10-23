from fastapi import APIRouter

router = APIRouter(
    prefix='/api',
    tags=['health-check'],
    responses={500: {"description": "Internal server error"}},
)


@router.get('/health-check')
async def health_check():
    return {'message': 'UP'}
