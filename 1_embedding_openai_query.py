#importing libraries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#creating an object of class 'OpenAIEmbeddings' with defined model
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

#calling 'embed_query' method to generate embedding query vector
result = embedding.embed_query("Delhi is the capital of India")

#printing embedding query vector
print(str(result))