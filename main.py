import secrets

from fastapi import FastAPI

from routes import public_router, private_router

app = FastAPI()

app.include_router(public_router)
app.include_router(private_router)
# token = secrets.token_hex(32)
# print(token)