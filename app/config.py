import os

from dotenv import load_dotenv


load_dotenv()


API_KEY_YANDEX = os.getenv("API_KEY_YANDEX")
PROMPT_ID = os.getenv("PROMPT_ID")
SERVICE_API_KEY = os.getenv("SERVICE_API_KEY")