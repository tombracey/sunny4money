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
    paragraphs = response.split('<<PARAGRAPH>>')
    
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    if len(paragraphs) >= 2:
        para1 = paragraphs[0]
        para2 = paragraphs[1]
        return para1, para2
    else:
      return response
    
ai_overview = gemini(f'Write 2 couple paragraphs split by <<PARAGRAPH>> to someone who is going to Paris with plane tickets costing £111. It is 8 degrees hotter than here in the UK. Talk about what a great destination it is, how they are getting a lot of sun for value and the unique attractions/history/culture. No preamble.')

print(ai_overview)
