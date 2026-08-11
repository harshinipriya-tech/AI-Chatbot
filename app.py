```python
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 My AI Chatbot")
st.write("Welcome! Ask me anything.")

# Connect to OpenAI using the secret stored in Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get new message
prompt = st.chat_input("Type your message here...")

if prompt:
    # Show user's message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Get AI response
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        answer = response.choices[0].message.content

    except Exception as e:
        answer = "Sorry, I couldn't connect to the AI service."

    # Show AI response
    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
```
