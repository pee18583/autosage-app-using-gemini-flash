import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key="AIzaSyDrauqt1oEL1EADnu8FkIns28khmREqVGA")

test_models = ['gemini-1.5-flash', 'gemini-flash-latest', 'gemini-pro-latest', 'gemini-1.5-pro']

print("Testing model availability and quota...")
for model_name in test_models:
    try:
        model = genai.GenerativeModel(model_name)
        # Attempt a very small generation to check quota
        response = model.generate_content("Hi", generation_config={"max_output_tokens": 1})
        print(f"SUCCESS: {model_name} is available and has quota.")
    except Exception as e:
        print(f"FAILED: {model_name} - {str(e)}")
