#Need to run following in venv before running actual code:
#huggingface-cli login --token (token_number)

#importing libraries
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#describing model and task under 'HuggingFaceEndpoint' class  
my_llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

#creating an object of class 'ChatHuggingFace' with defined model
model = ChatHuggingFace(llm = my_llm)

#calling 'invoke' method for query
result = model.invoke("What are the characteristics of a dog?")

#printing output
print(result.content)