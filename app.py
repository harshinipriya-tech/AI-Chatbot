import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 My AI Chatbot")
st.write("Welcome! Ask me anything.")

client = InferenceClient(
    token=st.secrets["HF_TOKEN"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = client.chat_completion(
            messages=st.session_state.messages,
            model="Qwen/Qwen2.5-7B-Instruct",
            max_tokens=500
        )

        answer = response.choices[0].message.content

    except Exception:
        answer = "Sorry, I couldn't connect to the AI service."

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
