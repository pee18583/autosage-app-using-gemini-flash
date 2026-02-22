import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = "AIzaSyDrauqt1oEL1EADnu8FkIns28khmREqVGA"
genai.configure(api_key=api_key)

print("Searching for a working model...")
working_models = []

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_name = m.name.split('/')[-1]
        try:
            model = genai.GenerativeModel(model_name)
            # Try a tiny generation
            model.generate_content("test", generation_config={"max_output_tokens": 1})
            print(f"ALIVE: {model_name}")
            working_models.append(model_name)
        except Exception as e:
            err = str(e)
            if "429" in err:
                print(f"QUOTA EXCEEDED: {model_name}")
            elif "404" in err:
                print(f"NOT FOUND: {model_name}")
            else:
                print(f"ERROR: {model_name} - {err[:100]}")

print("\nSummary of working models:")
for wm in working_models:
    print(f"- {wm}")

if not working_models:
    print("\nNo models found with quota. This API key may be completely exhausted or restricted.")
