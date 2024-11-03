import streamlit as st
from api_client import setup_client
from ui import display_sidebar, display_main_content
from utils import initialize_session_state, handle_user_input
from styles import small_button_css
def main():
    st.set_page_config(
    page_title="MathMate",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# A Math-Solving Chat App with NVIDIA API!"
    })
    st.markdown(small_button_css, unsafe_allow_html=True)  # Inject CSS styles
    client = setup_client()  # Set up the client
    initialize_session_state()  # Initialize session state
    display_sidebar()  # Display the sidebar
    display_main_content()  # Display ongoing conversation
    handle_user_input(client)  # Handle user input and response generation

if __name__ == "__main__":
    main()
