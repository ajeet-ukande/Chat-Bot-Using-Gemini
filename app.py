# import library
import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import google.generativeai as geneai


# load the environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")  # use the PAI Key from .env file
geneai.configure(api_key=api_key)

# Define model
# model = geneai.GenerativeModel('gemini-1.5-pro')

model = geneai.GenerativeModel('gemini-2.5-pro')


# Streamlit UI
st.set_page_config()
st.title("Ask Me Anythings...!")

# User input
text_input = st.text_input(label="Enter Your Query Here")
# text_input = st.text_area(label="Enter Your Query Here")

submit_button = st.button(label='Submit')

if submit_button:
    response = model.generate_content(text_input)
    st.write(response.text)

