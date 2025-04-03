import secrets

from fastapi import FastAPI

from routes import public_router

app = FastAPI()

app.include_router(public_router)
# token = secrets.token_hex(32)
# print(token)