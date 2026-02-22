import google.generativeai as genai
import os
from dotenv import load_dotenv

api_key = "AIzaSyASERDI6xHKNc1Uv_BBr40SNb2Cy4q6dGI"
genai.configure(api_key=api_key)

print("Checking models with new key...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_id = m.name # full name like models/gemini-1.5-flash
        model_short = m.name.split('/')[-1]
        try:
            model = genai.GenerativeModel(model_short)
            model.generate_content("hi", generation_config={"max_output_tokens": 1})
            print(f"WORKS: {model_short} (Full: {model_id})")
        except Exception as e:
            print(f"FAILED: {model_short} - {str(e)[:100]}")
