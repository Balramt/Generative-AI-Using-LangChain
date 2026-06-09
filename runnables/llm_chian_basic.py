from langchain_ollama import  ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic import LLMChain



model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


# Creates prompt

prompt= PromptTemplate(
    template='Write an summary on following text \n {text}',
    input_variables=['text']
)

# Create an LLm chain

chain = LLMChain(llm = model, prompt = prompt)

#run the chain with a specific topic'

topic = input('enter the topic name')

output = chain.run(topic)

print(output)

