from fastapi import FastAPI

from sql_app import models
from sql_app.database import engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
Import routes
"""
from router import user_routes, token_routes, account_routes, transaction_routes

app.include_router(token_routes.router)
app.include_router(user_routes.router)
app.include_router(account_routes.router)
app.include_router(transaction_routes.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
