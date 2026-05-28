from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama


model = ChatOllama( model="llama3.2:1b", temperature=0 )

messages = [
    SystemMessage(content = "You are help full assistance"),
    HumanMessage(content = "What is the capital of India")
]

result = model.invoke(messages)

messages.append(AIMessage(content= result.content))


print(messages)