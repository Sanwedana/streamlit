import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    st.error("API Key not found! Please check your .env file.")


