import asyncio
import json

from google import genai
from google.genai import types

from telegram import Bot

from src.schemas.PromotionData import PromotionData
from src.schemas.ProductData import ProductData

class TelegramService:

    def __init__(self):
        self.client = genai.Client(api_key="AQ.Ab8RN6JVHUG2zuVMUEUCIDtAlJM8gmKthucoUli4sG11Gs--Hg")

        self.telegram_token = "8559854372:AAHY2cerbSRJVgjB0pkUzt_MD_2OTVkWHnA"
        self.chat_id = "-5278291135"

        self.bot = Bot(token=self.telegram_token)

    def build_message(self, promotion: PromotionData, product: ProductData):

        prompt = f"""
        Você é um Copywriter de alta conversão para canais de ofertas rápidas no Telegram.
        Sua missão é criar uma copy extremamente curta, visual e direta ao ponto para o produto abaixo.
        O foco total deve ser no nome do produto, no preço irresistível e no desconto visual.

        Dados do Produto:
        Nome: {product.name}
        Categoria: {product.category}
        Link: {product.link}
        Avaliação: {product.assessment}
        Marca: {product.brand}
        Estoque: {product.stock}
        Quantidade vendida: {product.sales_quantity} 
        
        Dados da promoção:
        Preço antigo: {promotion.old_price}
        Preço atual: {promotion.actual_price}
        Desconto: {promotion.discount}
        Cupom: {promotion.coupon}

        Instruções Restritas de Estrutura:
        1. 'headline': Um título curto de uma linha com emojis chamativos e o nome do produto (Ex: "🔥 IMPERDÍVEL: Tênis Nike...").
        2. 'body': O corpo deve conter APENAS 3 a 4 linhas curtas em formato de lista (bullet points com emojis), mostrando de forma limpa:
           - O preço antigo vs. preço atual destacado.
           - O valor do desconto (porcentagem) ou se tem cupom disponível.
           - Uma única frase de gatilho rápido (Ex: "Avaliação {product.assessment}⭐" ou "Restam poucas unidades no estoque!").
           🚫 PROIBIDO escrever parágrafos longos, textos explicativos ou introduções cansativas.
        3. 'cta': Uma chamada para ação curtíssima de 1 linha (Ex: "🛒 Clique para garantir o seu:").

        Sua resposta DEVE ser estritamente um objeto JSON com os seguintes campos (use letras minúsculas):
        - 'headline'
        - 'body'
        - 'cta'
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

            #print(result_data)

            if not result_data:
                raise Exception("Falha no retorno da copy pela LLM")

            return result_data, product.link


        except Exception as e:
            print(f"Erro ao integrar com o Gemini: {e}")
            fallback_data = {
                "headline": "🔥 OFERTA IMPERDÍVEL!",
                "body": f"Aproveite para garantir o seu {product.name} com um preço especial.",
                "cta": "🛒 Garanta o seu antes que acabe:"
            }
            return fallback_data, product.link

    async def send_message(self, result_data, product_link):
        if not result_data:
            raise Exception("Falha no retorno da copy pela LLM")

        body_content = result_data['body']

        if isinstance(body_content, list):
            body_content = "\n".join(body_content)

        copy_complete = "\n".join([
            result_data['headline'],
            body_content,
            f" {result_data['cta']}\n👉 {product_link}"
        ])

        try:
            print("Enviando oferta para o Telegram...")
            await self.bot.send_message(
                    chat_id=self.chat_id,
                    text=copy_complete
            )
            print("Oferta enviada com sucesso")

            return True

        except Exception as e:
            print(f"Erro ao enviar para o Telegram: {e}")
            return False


    async def publish_offer(self, promotion: PromotionData, product: ProductData):
        result_data, product_link = self.build_message(promotion, product)

        if not await self.send_message(result_data, product_link):
            raise Exception("Erro ao enviar copy para o Telegram")
        else:
            return True