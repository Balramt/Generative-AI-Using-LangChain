from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()


hf_llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1-0528",
    task = "text-generation"
)

model = ChatHuggingFace(llm = hf_llm)

result = model.invoke("What is the capital of INDIA and Germany")

print(result.content)