import os
from dotenv import load_dotenv
import streamlit as streamL
import google.generativeai as gAI


load_dotenv('C:\\code\\python\\Google\\.env')
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("No GOOGLE_API_KEY found in the environment. Please check your .env file")

gAI.configure(api_key=api_key)
model = gAI.GenerativeModel('gemini-pro')


replacements = [("ian"),("edfrna"),("chelsea")]


streamL.title("Not Ian's Gemini Bot")

# Initialize chat history
if "messages" not in streamL.session_state:
    streamL.session_state.messages = [
        {
            "role":"assistant",
            "content":"Ask me Anything"
        }
    ]

# Display chat messages from history on app rerun
for message in streamL.session_state.messages:
    with streamL.chat_message(message["role"]):
        streamL.markdown(message["content"])

# Process and store Query and Response
def llm_function(query):
    response = model.generate_content(query)

    # Displaying the Assistant Message
    with streamL.chat_message("assistant"):
        streamL.markdown(response.text)

    # Storing the User Message
    streamL.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )

    # Storing the User Message
    streamL.session_state.messages.append(
        {
            "role":"assistant",
            "content": response.text
        }
    )

# Accept user input
query = streamL.chat_input("What's up?")

if query:
    for replacement in replacements:
        query = query.replace(replacement, "xxx")

# Calling the Function when Input is Provided
if query:
    # Displaying the User Message
    with streamL.chat_message("user"):
        streamL.markdown(query)

    llm_function(query)