import streamlit as st
import ollama
st.title("My AI ChatBot")
st.write("Welcome! Enter your question below.")
prompt = st.text_input(
    "Enter your prompt",
    placeholder="Ask me anything..."
)
if st.button("Send"):
    if prompt:
        response = ollama.chat(
            model="openchat",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        st.success("AI Response:")
        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a question.")