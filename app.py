### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables
import streamlit as st  # type: ignore
import os
import google.generativeai as genai # type: ignore
from PIL import Image

genai.configure(api_key="AIzaSyASERDI6xHKNc1Uv_BBr40SNb2Cy4q6dGI")



## Function to load Google Gemini Pro Vision API And get respon
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-flash-latest')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

##initialize our streamlit app
input_prompt="""
You are a automobile expert tasked with providing a detailed overview of any vehicles
The information should be presented in a structured format as follows:
Brand: Name of the vehicle brand.
Model: Specific model of the vehicle.
Launch year: Since when the Vehicle is available in market
Key Features: Describe the engine capacity, type (e.g., scooter, motorcycle, sedan, SUV), and special features(any top 3)
              (e.g., ABS, digital display, storage capacity, safety features).
Mileage: Provide the average mileage in km/l (kilometers per liter).
Average Price in INR: Mention the price range of the vehicle model.
Other Details: Include information on maintenance costs, additional benefits, and any unique selling points.
Approximate Resale Value: Estimate the resale value of the vehicle after 10 years in Indian Rupees.
"""
st.set_page_config(page_title='Welcome')
st.header('AutoSage App')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit=st.button('Submit')
if submit:
    image_data=input_image_setup(uploaded_file)
    response= get_gemini_response(input_prompt, image_data)
    st.header('The details about the Vehicle are as follow:')
    st.write(response)
