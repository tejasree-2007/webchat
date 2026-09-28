import streamlit as st
from ollama import chat
st.title("My AI ChatBot:")
#messages =[]
system_message = "You are a tutor.Answer a sentence in a 50 words max."
#messages.append({
#   "role":"system",
#  "content":system_message
#})
if "messages" not in st.session_state:
    st.session_state.messages = [
    {
        "role":"system",
        "content":system_message
    }
    ]
#Display previous messages
for msg in st.session_state.messages:
    #Don't diplay system message
    if msg["role"]!= "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

question = st.chat_input("Ask something...")
if question:
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({
        "role":"user",
        "content":question
    })  
    with st.spinner("Thinking..."):
        response = chat(model="gemma3:1b", messages=st.session_state.messages)
        answer = response.message.content
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append({
            "role":"assistant",
            "content":answer
        })