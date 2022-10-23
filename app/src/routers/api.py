from fastapi import APIRouter
from app.src.routers import health_check, send_ticket, get_records

router = APIRouter()
router.include_router(health_check.router)
router.include_router(send_ticket.router)
router.include_router(get_records.router)
