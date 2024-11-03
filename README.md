

# Math Solving Chat App with NVIDIA API

## Overview
This is a chat application built with Streamlit that allows users to engage in chat sessions, manage chat history, and solve math-related queries using the NVIDIA API. The app provides a simple and interactive interface for managing multiple chat sessions.

## Features
- Start and manage multiple chat sessions.
- View chat history with options to select and delete chats.
- An intuitive sidebar for easy navigation.
- Displays math-solving responses from the NVIDIA API.

## Quick Reference Guide

### Python Virtual Environment
1. **Create a New Virtual Environment:**
   ```sh
   python -m venv venv
   ```
2. **Activate the Virtual Environment:**
   ```sh
   # Windows
   venv\Scripts\activate
   # Unix/macOS
   source venv/bin/activate
   ```
3. **Deactivate the Environment:**
   ```sh
   deactivate
   ```

### Package Management
1. **List Installed Packages:**
   ```sh
   pip list
   ```
2. **Save Packages to `requirements.txt`:**
   ```sh
   pip freeze > requirements.txt
   ```
3. **Install Packages from `requirements.txt`:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Uninstall a Package:**
   ```sh
   pip uninstall package_name
   ```

### Running the App
1. **Start the Streamlit Application:**
   ```sh
   streamlit run app.py
   ```

### Git Commands
1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   ```
2. **Check the Status of Your Repository:**
   ```sh
   git status
   ```
3. **Add Changes to Staging:**
   ```sh
   git add .
   ```
4. **Commit Changes:**
   ```sh
   git commit -m "Your commit message"
   ```
5. **Push Changes to Remote:**
   ```sh
   git push origin main
   ```

### Docker Commands (If applicable)
1. **Build Docker Image:**
   ```sh
   docker build -t chatapp:local .
   ```
2. **Run Docker Container:**
   ```sh
   docker run -p 8501:8501 chatapp:local
   ```

### Caution
- **Do not push** sensitive data or secrets to public repositories.
- Use `.gitignore` to avoid committing unnecessary files and sensitive information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to Streamlit and NVIDIA for their powerful tools that made this project possible.

