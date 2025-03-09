#importing libraries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#creating an object of class 'OpenAIEmbeddings' with defined model
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

#defining document to generate embedding document vector
documents = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France."
]

#calling 'embed_documents' method to generate embedding document vector
result = embedding.embed_documents(documents)

#printing embedding document vector
print(str(result))