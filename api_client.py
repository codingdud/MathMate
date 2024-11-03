from openai import OpenAI
import streamlit as st

def setup_client():
    return OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=st.secrets["NVIDIA_API_KEY"]
    )
