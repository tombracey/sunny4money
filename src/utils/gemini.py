import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def gemini(prompt):
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    request = model.generate_content(prompt)
    response = request.to_dict()["candidates"][0]["content"]["parts"][0]["text"]
    return response