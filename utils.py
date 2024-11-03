import streamlit as st
from chat_history import load_chat_history, save_chat_history
import time

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = load_chat_history()  # Load existing chat history
    if "history_load_error" not in st.session_state:
        st.session_state.history_load_error = False
    if "title_displayed" not in st.session_state:
        st.session_state.title_displayed = False
    if "chat_name" not in st.session_state:
        st.session_state.chat_name = "Chat 1"  # Default chat name
        st.session_state.messages[st.session_state.chat_name] = []  # Initialize the message list

def handle_user_input(client):
    prompt = st.chat_input("Ask a math question here")
    if prompt:
        st.session_state.messages[st.session_state.chat_name].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        response_text = generate_response(client)
        if response_text:
            st.session_state.messages[st.session_state.chat_name].append({"role": "assistant", "content": response_text})
        save_chat_history(st.session_state.messages)  # Save updated chat history

def generate_response(client):
    response_text = ""
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[st.session_state.chat_name]],
        temperature=0.5,
        max_tokens=1024,
        stream=True
    )
    with st.chat_message("assistant"):
        placeholder = st.empty()
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
                placeholder.markdown(response_text)
                time.sleep(0.05)
    return response_text
