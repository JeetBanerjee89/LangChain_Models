#importing libraries
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#creating an object of class 'ChatOpenAI' with defined model
model = ChatOpenAI(model = 'gpt-4', temperature = 0, max_completion_tokens = 100)

#calling 'invoke' method for query
result = model.invoke("Write 5 line poem on India")

#printing output
print(result.content)