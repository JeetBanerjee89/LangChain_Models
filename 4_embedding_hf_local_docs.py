#Need to run following in venv before running actual code:
#huggingface-cli login --token (token_number)

#importing libraries
from langchain_huggingface import HuggingFaceEmbeddings

#creating an object of class 'HuggingFaceEmbeddings' with defined model
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

#defining document to generate embedding document vector
document = [
    "Cricket is a bat-and-ball game played between two teams of eleven players on a field.",
    "Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.",
    "Hockey is a term used to denote a family of various types of both summer and winter team sports which originated on either an outdoor field, sheet of ice, or dry floor such as in a gymnasium.",
    "Volleyball is a team sport in which two teams of six players are separated by a net.",
    "Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball"
]

#calling 'embed_documents' method to generate embedding document vector
vector = embedding.embed_documents(document)

#printing embedding document vector
print(str(vector))