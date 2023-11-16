import streamlit as st
from openai import OpenAI
import time 

st.set_page_config(layout="wide")
# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Initialize the messages state if not already present
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Initialize the annotations state if not already present
if 'annotations' not in st.session_state:
    st.session_state.annotations = []
    
# Create a new thread for the conversation
if 'thread' not in st.session_state:
    st.session_state.thread = client.beta.threads.create()
thread = st.session_state.thread

assistant_id = st.secrets["assistant_id"]
if 'assistant' not in st.session_state:
    st.session_state.assistant = client.beta.assistants.retrieve(assistant_id)
assistant = st.session_state.assistant


def append_annotation(new_annotation):
    # Check if the annotation text is already in the session state
    if new_annotation.text not in [annot['text'] for annot in st.session_state.annotations]:
        # Append the new annotation if it's unique
        annotation_dict = {
            'text': new_annotation.text,
            'citation': new_annotation.file_citation.quote
        }
        st.session_state.annotations.append(annotation_dict)


col1, col2 = st.columns([2,1])
# Display the annotations in a separate, persistent section
with col2:
    with st.container():
        st.write("Källor:")
        for annotation in st.session_state.annotations:
            with st.expander(annotation['text']):
                st.markdown(annotation['citation'])

with col1:
    # st.write(thread.id)
    st.title(assistant.name)
    st.markdown(assistant.description)

    # Display the chat history
    for message in st.session_state.messages:
        role, content = message["role"], message["content"]
        with st.chat_message(role):
            st.markdown(content)

# Handle user input
user_input = st.chat_input("Skicka meddelande till boten...")
if user_input:
    
    # Add user input to messages and display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with col1:
        with st.chat_message("user"):
            st.markdown(user_input)

    # Add message to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        # instructions="Please address the user as Frej Andreassen. The user has a premium account."
    )

    with st.spinner('Processing....'):
        # Wait for the assistant to respond
        polls = 0
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status in ['completed', 'failed']:
                break
            polls += 1
            if (polls > 50): break
            time.sleep(1)  # Sleep for a second before checking again
    
    # Display the assistant's response
    if run_status.status == 'completed':
        # Get the messages here:
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        
        # Display each new message from the assistant
        message = messages.data[0]
        if message.role == "assistant":
            content = message.content[0].text.value
            # Process and store annotations
            annotations = message.content[0].text.annotations
            for annotation in annotations:
                append_annotation(annotation)

            st.session_state.messages.append({"role": "assistant", "content": content})
            with col1:
                with st.chat_message("assistant"):
                    st.markdown(content)

