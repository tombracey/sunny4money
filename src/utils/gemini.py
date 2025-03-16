import google.generativeai as genai

def gemini(prompt):
    gemini_api_key = 'AIzaSyC_oY47M5uub372sCdDQN-pOX4FdTjGkzI'
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    request = model.generate_content(prompt)
    response = request.to_dict()["candidates"][0]["content"]["parts"][0]["text"]
    return response