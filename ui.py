import streamlit as st
from chat_history import load_chat_history, save_chat_history


# Display sidebar with chat options
def display_sidebar():
    with st.sidebar:
        st.header("MathMate")

        # Initialize messages from file or session state
        if 'messages' not in st.session_state:
            st.session_state.messages = load_chat_history()

        # Display current chat name
        if 'chat_name' in st.session_state:
            st.subheader(f"Current Chat: {st.session_state.chat_name}")

        # Text input for new chat name, shown conditionally after clicking "New Chat" button
        if st.button("New Chat", key="new_chat"):
            st.session_state.show_new_chat_input = True

        if st.session_state.get("show_new_chat_input"):
            new_chat_name = st.text_input("Enter a name for the new chat:", key="new_chat_name_input")
            if new_chat_name:
                st.session_state.chat_name = new_chat_name
                st.session_state.messages[new_chat_name] = []
                st.toast(f"Starting a new chat: {new_chat_name}. Ask your question.", icon="✅")
                save_chat_history(st.session_state.messages)  # Save new chat
                st.session_state.show_new_chat_input = False  # Reset the new chat input

        # Display chat names and allow selection and deletion
        display_chat_names()
        
        # Display individual chat messages
        display_chat_history()
# Display chat names with delete options
def display_chat_names():
    if st.session_state.messages:
        st.subheader("Available Chats:")

        chat_names = list(st.session_state.messages.keys())
        for chat_name in chat_names:
            cols = st.columns([2, 1])  # Two columns: chat name and delete icon
            with cols[0]:
                if st.button(chat_name, key=f"chat_{chat_name}", use_container_width=True):
                    st.session_state.chat_name = chat_name
                    st.toast(f"Switched to chat: {chat_name}.", icon="✅")
            with cols[1]:
                delete_icon = "🗑️"
                if st.button(delete_icon, key=f"delete_{chat_name}", help="Delete chat", use_container_width=True):
                    del st.session_state.messages[chat_name]  # Delete chat
                    if st.session_state.chat_name == chat_name:
                        st.session_state.chat_name = None
                    st.toast(f"Deleted chat: {chat_name}.", icon="🗑️")
                    save_chat_history(st.session_state.messages)  # Save changes to file
    else:
        st.write("No chats available.")

# Display chat history for the current chat
def display_chat_history():
    st.subheader("Chat History:")
    if 'chat_name' in st.session_state and st.session_state.chat_name in st.session_state.messages:
        for index, message in enumerate(st.session_state.messages[st.session_state.chat_name]):
            content_preview = ' '.join(message['content'].split()[:2])
            content_preview += "..." if len(message['content'].split()) > 10 else ""
            if st.button(f"{message['role']}: {content_preview}", key=f"msg_{index}"):
                st.session_state.message = message
                st.session_state.show_full_message = True
    else:
        st.write("No chat history available.")

# Main content display
def display_main_content():
    if not st.session_state.get('title_displayed', False):
        st.title("Math Solving Chat App with NVIDIA API")
        st.session_state.title_displayed = True

    for message in st.session_state.messages.get(st.session_state.chat_name, []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])