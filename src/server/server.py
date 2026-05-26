from fastapi import FastAPI
from routes.products_routes import products_routes

app = FastAPI()

app.include_router(products_routes)