from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sql_app import models
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(CORSMiddleware, allow_origins=['*'])
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
