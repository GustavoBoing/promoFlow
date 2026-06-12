import asyncio
import json

from google import genai
from google.genai import types

from telegram import Bot

from src.schemas.PromotionData import PromotionData
from src.schemas.ProductData import ProductData

class TelegramService:

    def __init__(self):
        self.client = genai.Client()

        self.telegram_token = "8559854372:AAHY2cerbSRJVgjB0pkUzt_MD_2OTVkWHnA"
        self.chat_id = "-5278291135"

        self.bot = Bot(token=self.telegram_token)

    def build_message(self, promotion: PromotionData, product: ProductData):

        prompt = f"""
        Você é um Copywriter profissional de alta conversão, especializado em e-commerce e canais de ofertas (como Telegram e WhatsApp).
        Sua missão é criar uma copy de vendas altamente persuasiva e irresistível para o produto abaixo, focando nos benefícios e na oportunidade do preço.
        
        Dados do Produto:
        Nome:{product.name}
        Categoria: {product.category}
        Link: {product.link}
        Avaliação: {product.assessment}
        Marca: {product.brand}
        Estoque: {product.stock}
        Quantidade vendida:{product.sales_quantity} 
        
        Dados da promoção:
        Preço antigo: {promotion.old_price}
        Preço atual: {promotion.actual_price}
        Desconto: {promotion.discount}
        Cupom: {promotion.coupon}
        
        Instruções da Estrutura da Copy:
        1. Comece com um gancho/headline curto e impactante usando Emojis (ex: "🔥 ALERTA DE MENOR PREÇO!").
        2. Destaque por que esse produto vale a pena (foque nas principais dores que ele resolve ou no desejo do cliente).
        3. Use um gatilho de urgência ou escassez relacionado ao preço baixo.
        4. Finalize com uma chamada para ação (CTA) clara para o usuário clicar no link da oferta.
        5. Mantenha o tom dinâmico, moderno e direto ao ponto.
        
        Sua resposta DEVE ser estritamente um objeto JSON com os seguintes campos (use letras minúsculas):
        - 'headline': Um título curto e chamativo com emojis.
        - 'body': O corpo do texto da copy formatado com quebras de linha (\\n) onde for necessário.
        - 'cta': A frase final de chamada para a ação.
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            result_data = json.loads(response.text)

            if not result_data:
                raise Exception("Falha no retorno da copy pela LLM")

            return result_data, product.link


        except Exception as e:
            print(f"Erro ao integrar com o Gemini: {e}")
            return {"copy:": None, "Justification": "Falha ao gerar copy via LLM."}

    def send_message(self, result_data, product_link):
        if not result_data:
            raise Exception("Falha no retorno da copy pela LLM")

        copy_complete = "\n".join([
            result_data['headline'],
            result_data['body'],
            result_data['cta'],
            product_link
        ])

        try:
            print("Enviando oferta para o Telegram...")
            asyncio.run(
                self.bot.send_message(
                    chat_id=self.chat_id,
                    text=copy_complete
                )
            )
            print("Oferta enviada com sucesso")

            return True

        except Exception as e:
            print(f"Erro: {e}")
            return False


    def publish_offer(self, promotion: PromotionData, product: ProductData):
        result_data, product_link = self.build_message(promotion, product)

        if not self.send_message(result_data, product_link):
            raise Exception("Erro ao enviar copy para o Telegram")
        else:
            promotion.publish = True
            return True
