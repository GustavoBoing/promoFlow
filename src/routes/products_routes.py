from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.product_create import ProductCreate
from fastapi.encoders import jsonable_encoder

products_routes = APIRouter(tags=["Products"])

@products_routes.post("/products")
async def create_product(body: ProductCreate):
    dict_body = jsonable_encoder(body)
    return JSONResponse(
        status_code= 201,
        content= {
            "message": "Produto criado com sucesso",
            "att": dict_body
        }
    )