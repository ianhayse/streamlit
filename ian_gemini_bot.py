import os
import streamlit as streamL
import google.generativeai as gAI

os.environ['GOOGLE_API_KEY'] = streamL.secrets["GOOGLE_API_KEY"]
gAI.configure(api_key = os.environ['GOOGLE_API_KEY'])

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