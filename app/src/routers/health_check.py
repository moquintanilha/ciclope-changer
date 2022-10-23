from fastapi import APIRouter

router = APIRouter(
    prefix='/api',
    tags=['health-check'],
    responses={404: {"description": "Not found"}},
)


@router.get('/health-check')
async def health_check():
    return {'message': 'UP'}
