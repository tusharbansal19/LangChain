from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the Google Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Invoke the model with a question
response = model.invoke("Who is the CEO of Google?")

print(response.content)
