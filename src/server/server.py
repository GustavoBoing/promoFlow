from fastapi import FastAPI
from routes.OffersRoutes import offers_routes


app = FastAPI()

app.include_router(offers_routes)