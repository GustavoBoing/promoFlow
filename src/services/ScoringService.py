import os
import json
from google import genai
from google.genai import types

class ScoringService:

    def __init__(self):
        self.client = genai.client

    def calculate_score(self, product_name: str, product_assessment: float, ):


        pass

    #definir regras de score
    #integrar LLM para que ela consiga validar o score de cada produto de acordo com informações complexas