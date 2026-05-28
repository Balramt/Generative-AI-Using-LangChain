from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


model = ChatOllama( model="llama3.2:1b", temperature=0 )

chat_history = [
    SystemMessage(content= "YOu are helpfull AI assistant")
]


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == "Exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)