
# Multi-Page Streamlit App for AI Assistant Management and Chat

This Streamlit application is designed to manage an AI Assistant and facilitate chat interactions. It consists of two main pages: `Home.py` and `pages/chat.py`.

## Home.py

This page is dedicated to managing the AI Assistant's information and files. It allows users to update the assistant's details and manage custom knowledge base files associated with the assistant.

### Features

- **Update Assistant Information**: Modify the name, description, and instructions of the AI Assistant.
- **Assistant File Management**: View and delete existing files in the assistant's knowledge base. Additionally, users can upload new files with specific allowed extensions.

### Allowed File Extensions

The application supports various file extensions for upload, including `.c`, `.cpp`, `.csv`, `.docx`, `.html`, `.java`, `.json`, `.md`, `.pdf`, `.php`, `.pptx`, `.py`, `.rb`, `.tex`, `.txt`.

## pages/chat.py

This page facilitates a chat interface with the AI Assistant. It displays the assistant's responses and any annotations in a structured format.

### Features

- **Chat Interface**: Send messages to the AI Assistant and view its responses.
- **Annotations Display**: Annotations provided by the AI Assistant are displayed in a separate column, offering additional information and context to the user.
- **Persistent Annotations**: Annotations are stored in the session state, ensuring they persist throughout the interaction.

## Installation and Setup

To run this application:

1. Ensure you have Python and Streamlit installed.
2. Clone this repository.
3. Navigate to the app directory.
4. Run `streamlit run Home.py` to start the application.
5. Switch between the "Home" and "Chat" pages using the sidebar menu.

## Configuration

Before running the app, make sure to set up your OpenAI API key and Assistant ID in `st.secrets`. This is essential for the application to interact with the OpenAI API.

## Usage

Navigate through the application using the sidebar. On the "Home" page, you can manage the AI Assistant's information and files. On the "Chat" page, engage in conversations with the assistant and view annotations.

