from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Qwen2.5-72B-Instruct is available on HuggingFace free Serverless Inference API
endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    max_new_tokens=70,
)

model = ChatHuggingFace(llm=endpoint)
while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = model.invoke(question)

    print("\nAI:", response.content)

