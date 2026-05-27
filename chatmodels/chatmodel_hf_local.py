from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


local_LLm = HuggingFacePipeline.from_model_id(
    model_id= "deepseek-ai/DeepSeek-R1-0528",
    task = "text-generation",
    pipeline_kwargs= dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
    
)

model = ChatHuggingFace(local_LLm)

result = model.invoke("What is the capital of INdia and Germany?")

print(result.content)

