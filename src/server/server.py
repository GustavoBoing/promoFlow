from fastapi import FastAPI
from src.routes.OffersRoutes import offers_routes
from src.routes.app import app_route

app = FastAPI(title="Promoflow Backend")

app.include_router(offers_routes)
app.include_router(app_route)