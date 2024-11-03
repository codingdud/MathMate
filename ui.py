import streamlit as st

def display_sidebar():
    with st.sidebar:
        st.header("Chat App")  # Sidebar header
        
        # Initialize messages dictionary if it doesn't exist
        if 'messages' not in st.session_state:
            st.session_state.messages = {}
        
        # Display the current chat name
        if 'chat_name' in st.session_state:
            st.subheader(f"Current Chat: {st.session_state.chat_name}")  # Show current chat name
        
        # Button to start a new chat
        if st.button("New Chat", key="new_chat"):
            new_chat_name = st.text_input("Enter a name for the new chat:", value=f"Chat {len(st.session_state.messages) + 1}")
            if new_chat_name:
                st.session_state.chat_name = new_chat_name  # Update the chat name
                st.session_state.messages[st.session_state.chat_name] = []  # Initialize new message list
                st.session_state.title_displayed = False  # Reset title display flag
                st.toast(f"Starting a new chat: {new_chat_name}. Ask your question.", icon="✅")

        # Display chat names and allow selection and deletion
        st.write("### Chat History")
        display_chat_names()

def display_chat_names():
    # Show all available chat names
    if st.session_state.messages:
        st.subheader("Available Chats:")
        
        chat_names = list(st.session_state.messages.keys())  # Create a list of chat names
        for chat_name in chat_names:
            cols = st.columns([2, 1])  # Create two columns: one for the chat name, one for the delete icon
            with cols[0]:
                if st.button(chat_name, key=f"chat_{chat_name}",use_container_width=True):
                    st.session_state.chat_name = chat_name  # Switch to selected chat
                    st.session_state.title_displayed = False  # Reset title display flag
                    st.toast(f"Switched to chat: {chat_name}.", icon="✅")
            with cols[1]:
                # Display a delete icon with a button
                delete_icon = "🗑️"  # Icon for delete action
                if st.button(delete_icon, key=f"delete_{chat_name}",use_container_width=True):
                    del st.session_state.messages[chat_name]  # Delete the chat
                    # Reset current chat name if it was deleted
                    if st.session_state.chat_name == chat_name:
                        st.session_state.chat_name = None
                    st.toast(f"Deleted chat: {chat_name}.", icon="🗑️")
    else:
        st.write("No chats available.")



def display_main_content():
    if not st.session_state.title_displayed:
        st.title("Math Solving Chat App with NVIDIA API")
        st.session_state.title_displayed = True

    # Display messages for the current chat in the main content area
    for message in st.session_state.messages.get(st.session_state.chat_name, []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# To run the app, you would typically call display_sidebar() and display_main_content() in your main app logic
