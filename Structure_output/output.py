from typing import Optional
from pydantic import Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import json
# from typing import TypedDict


#----------------------------
# class output_formate(TypedDict):
#     summary: str
#     sentiment: str

#----------------------------
# class output_formate(BaseModel):
#     summary: str=Field(description="a brief summary")
#     sentiment: str=Field(description="positive or negative or Neutral")
#     topic: str=Field(description="main topics")
#     keywords: list[str]=Field(description="list of keywords")
#     writer: Optional[str]=Field(description="writer name")



# print(output_formate)
load_dotenv()
output_formate={}
with open("model.json") as f:
    output_formate=json.load(f)
endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    max_new_tokens=70,
)

model = ChatHuggingFace(llm=endpoint)
model=model.with_structured_output(dict(output_formate))

result=model.invoke("Arceus is known in Pokémon lore as the creator of the entire Pokémon universe. According to legends from the Pokémon Diamond, Pokémon Pearl, and Pokémon Legends: Arceus, Arceus emerged from a cosmic egg in a place of nothingness before time and space existed. After awakening, it shaped reality by creating powerful Pokémon that would govern the universe: Dialga to control time, Palkia to rule over space, and Giratina to represent antimatter and the Distortion World. Arceus also created the guardians of knowledge, emotion, and willpower—Uxie, Mesprit, and Azelf—who helped shape human consciousness. From this divine creation, the world of Pokémon, nature, and life began to evolve, leading to the countless Pokémon species seen today. Because of this role, Arceus is often called “The Original One”, the mythical being believed to be the origin of all Pokémon and the universe itself.  given by Tushar bansal")

print(result)    
    