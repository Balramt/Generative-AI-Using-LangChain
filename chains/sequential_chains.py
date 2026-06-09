from langchain_ollama import  ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


prompt1 = PromptTemplate(
    template = 'Generates a detailed report on {topic}',
    input_variables= ['topic']
)



prompt2 = PromptTemplate(
    template = 'Generates a 2 pointer summary from the following text \n {text}',
    input_variables= ['text']
)


parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'AI uses in IT industry'})


print(result)

chain.get_graph().print_ascii()

