from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.database.Database import SessionLocal
from src.schemas.OffersRequest import OffersRequest
from fastapi.encoders import jsonable_encoder
from src.services.OfferService import OfferService

offers_routes = APIRouter(tags=["Offers"])

@offers_routes.post("/offers")
async def create_offer(body: OffersRequest):
    db = SessionLocal()
    service = OfferService(db)
    await service.process_offer(body)
    dict_body = jsonable_encoder(body)

    db.close()

    return JSONResponse(
        status_code= 201,
        content= {
            "message": "Oferta criado com sucesso",
            "att": dict_body
        }
    )