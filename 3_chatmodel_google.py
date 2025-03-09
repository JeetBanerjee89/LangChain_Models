#importing libraries
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#creating an object of class 'ChatGoogleGenerativeAI' with defined model
model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

#calling 'invoke' method for query
result = model.invoke('Tell me 5 Indian criketers names from Karnataka')

#printing output
print(result.content)