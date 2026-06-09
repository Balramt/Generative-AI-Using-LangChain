from langchain_ollama import  ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


prompt = PromptTemplate(
    template = 'Generates 5 interesting facts about {topic}',
    input_variables= ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result)

chain.get_graph().draw_ascii()

