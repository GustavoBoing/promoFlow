from fastapi import FastAPI
from src.routes.OffersRoutes import offers_routes
from src.routes.app import app_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Promoflow Backend")

app.include_router(offers_routes)
app.include_router(app_route)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)