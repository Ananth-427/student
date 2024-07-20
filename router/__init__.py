from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router.spost import get_data


def create_app():
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(get_data)  # todo: add router here

    @app.get("/")
    def home():
        return "Hello World!"

    return app