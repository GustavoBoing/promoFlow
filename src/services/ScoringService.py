import os #Lê variáveis de ambiente
import json # Manipular o formato JSON, ela transforma o texto puro do gemini em um dicionario Python
from google import genai # Permite o acesso os modelos do Gemini
from google.genai import types

class ScoringService:

    def __init__(self):
        #O cliente busca automaticamente a variável de ambiente GEMINI_API_KEY
        self.client = genai.Client()

    def calculate_score(self, product_name: str, product_assessment: float,
                        product_stock: int, product_qtde_sales: int, promotion_old_price: float,
                        promotion_actual_price: float, promotion_discount: float, promotion_coupon: str) -> dict:
        prompt = f"""
        Você é o motor de inteligência do sistema Promoflow.
        Analise o produto abaixo e gere um score de atratividade de 0 a 100 (apenas numeros inteiros)
        
        Critérios:
        - Porcentagem de desconto real
        - Apelo comercial do título do produto
        - Boa avaliação dos consumidores do produto
        - O produto deve ter sido vendido pelo menos uma vez
        - Um estoque baixo para uma quantidade de vendas alta significa um bom sinal 
        - Um produto que tem desconto e tem cupom é um bom sinal
        
        Dados do produto:
        - Titulo: {product_name}
        - Avaliação: {product_assessment}
        - Estoque: {product_stock}
        - Quantidade de vendas: {product_qtde_sales}
        - Preço antigo: R$ {promotion_old_price:.2f}
        - Preco atual: R$ {promotion_actual_price:.2f}
        - Desconto: {promotion_discount:.1f}%
        - Cupom: {promotion_coupon}
        
        Sua resposta DEVE ser estritamente um objeto JSON com os campos 'score' (inteiro) e 'justification' (string curta).
        """
        try:
            #Função que envia os dados para o Gemini
            response = self.client.models.generate_content(
                model='gemini-2.5-flash', #modelo da LLM
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json" # Isso avisa o gemini: "Não me entregue textinhos e sim, apenas o JSON"
                ),
            )

            result_data = json.loads(response.text) #Processa os dados
            return result_data #Retorna os dados

        except Exception as e:
            print(f"Erro ao integrar com o Gemini: {e}")
            return {"score": None, "Justification:": "Falha ao gerar score via LLM."}

    #definir regras de score
    #integrar LLM para que ela consiga validar o score de cada produto de acordo com informações complexas