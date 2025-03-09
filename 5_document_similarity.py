#importing libraries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#fetching API key
load_dotenv()

#creating an object of class 'OpenAIEmbeddings' with defined model
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 300)

#defining document 
document = [
    "Cricket is a bat-and-ball game played between two teams of eleven players on a field.",
    "Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.",
    "Hockey is a term used to denote a family of various types of both summer and winter team sports which originated on either an outdoor field, sheet of ice, or dry floor such as in a gymnasium.",
    "Volleyball is a team sport in which two teams of six players are separated by a net.",
    "Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball"
]

#defining user query
query = "Tell me about basket game"

#generating embeddings vector for both document and user query
doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

#calculating 'cosine_similarity' b/w query_embedding_vector and document_embedding_vector
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

#fetching index and score for highest cosine_similarity
index, score = sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]

#printing most relevant match from document data for a user query
print("Query: ", query)
print("AI Assitant: ", document[index])
print("Similarity Score: ", score)