import os
from dotenv import load_dotenv

load_dotenv()

LLM_KEY = os.getenv('LLM_KEY')
DATA_KEY = os.getenv('DATA_KEY')
LLM_URL = os.getenv('LLM_URL')
MODEL = os.getenv('MODEL')