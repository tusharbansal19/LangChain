from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize the HuggingFaceEmbeddings model
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

with open("pokemon_description.json", "r") as f:
    data = json.load(f)
    response = model.embed_documents(data)
    with open("pokemon_description.json", "w") as f1:
        json.dump(response, f1)
    print(response)