import streamlit as st
from ollama import chat
st.title("my AI bot: synora")
name="TEJA"
st.write("Welcome, ",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    #st.write("You asked: ", question)
    response = chat(model ="gemma3:1b", messages = [{
        "role": "system", 
        "content": "you are a friendly tutor, you explain concepts in a very simple way, Explain in 50 words max"
        }, 
        {"role": "user", 
         "content": question
        }
    ])
    answer = response.message.content
    st.write(f"Answer: {answer}")
#dropdown
options = ["C++","Java","Python"]
choice = st.selectbox("select your favorite language: ", options)
st.write(f"You selected: {choice}")