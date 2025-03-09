#importing libraries
from langchain_openai import OpenAI
from dotenv import load_dotenv

#loading OpenAI API Key
load_dotenv()

#creating object of class 'OpenAI' with a defined model
llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

#calling 'invoke' method for a user query
result = llm.invoke("Who is the Prime Minister of India?")

#printing output
print(result)