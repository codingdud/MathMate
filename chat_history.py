import json
import os
import streamlit as st

def load_chat_history():
    if os.path.exists("chat_history.json"):
        with open("chat_history.json", "r") as file:
            return json.load(file)
    return {}

def save_chat_history(messages):
    with open("chat_history.json", "w") as file:
        json.dump(messages, file)
