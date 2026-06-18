from src.database.Database import SessionLocal
from src.schemas.OffersRequest import OffersRequest
from src.services.OfferService import OfferService


class PipelineService:
    def __init__(self, offers: list[OffersRequest]):
        self.offers = offers
        self.db = SessionLocal()
        self.offer_service = OfferService(self.db)

    async def run(self):
        print("Iniciando a pipeline")


        try:
            for offer in self.offers:
                try:
                    await self.offer_service.process_offer(offer)

                except Exception as e:
                    print(f"Erro ao processar oferta {offer}: {e}")
                    self.db.rollback()
        finally:
            print("Fechando a conexão com o banco de dados")
            self.db.close()

        print("Pipeline finalizada")