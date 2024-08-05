import streamlit as st
import requests


# Function to send message to Flask API
def send_message(message):
    url = "http://localhost:5000/chat"
    data = {"message": message,}
    response = requests.post(url, json=data)
    return response.json().get('response', 'Error: No response from server.')

st.title("Loja ABC")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and send message
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user message to the API and get the response
    response = send_message(prompt)

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Append the assistant's response to the session state messages
    st.session_state.messages.append({"role": "assistant", "content": response})