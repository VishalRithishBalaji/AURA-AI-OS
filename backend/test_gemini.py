import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv("../.env")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello AURA AI")

print(response.text)
