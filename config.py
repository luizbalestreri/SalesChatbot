import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_URL = os.getenv('API_URL')