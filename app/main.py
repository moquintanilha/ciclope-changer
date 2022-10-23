"""Run FastAPI app."""
from fastapi import FastAPI
from app.src.routers.api import router as api_router


def main():
    app = FastAPI()
    app.include_router(api_router)
    return app


if __name__ == "__main__":
    main()
