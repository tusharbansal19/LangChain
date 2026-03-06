from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the HuggingFaceEmbeddings model
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

response = model.embed_query("delhi is good city")
print(response)