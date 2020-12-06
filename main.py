from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sql_app import models
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Import routes
"""
from controller import user, token, account, transaction

app.include_router(token.router)
app.include_router(user.router)
app.include_router(account.router)
app.include_router(transaction.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
