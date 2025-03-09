#Need to run following in venv before running actual code:
#huggingface-cli login --token (token_number)

#importing libraries
from langchain_huggingface import HuggingFaceEmbeddings

#creating an object of class 'HuggingFaceEmbeddings' with defined model
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

#defining text to generate embedding text vector
text = "Kolkata is the capital of West Bengal."

#calling 'embed_query' method to generate embedding query vector
vector = embedding.embed_query(text)

#printing embedding query vector
print(str(vector))