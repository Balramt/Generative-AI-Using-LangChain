from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate


model = ChatOllama( model="llama3.2:1b", temperature=0 )

#result = model.invoke("What is the capital of India?")

#print(result.content)


st.header("Research Tool")

user_input = st.text_input("Enter your Query ?")

if st.button('Sumarize'):
    result = model.invoke(user_input)
    st.write(result.content)


