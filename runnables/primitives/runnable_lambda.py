
from langchain_ollama import  ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda



def word_counter(text):
    return len(text.split())


model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

gen_joke_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'num_words': RunnableLambda(word_counter)   # RunnableLambda(lambda X: len(x.split()))  # Here we make the word counter method as runnable
})

final_chain = RunnableSequence(gen_joke_chain,parallel_chain)

result = final_chain.invoke({'topic': 'cricket'})

print("joke", result['joke'])
print("num_words", result['num_words'])


