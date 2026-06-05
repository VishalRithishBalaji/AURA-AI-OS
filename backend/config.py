from dotenv import load_dotenv
import os

load_dotenv("../.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
