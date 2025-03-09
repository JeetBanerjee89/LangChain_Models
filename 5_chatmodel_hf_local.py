#Need to run following in venv before running actual code:
#huggingface-cli login --token (token_number)

#importing libraries
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

#defining local folder for model download
os.environ['HF_HOME'] = 'D:/huggingface_cache'

#describing model, task and other keyword_arguments under 'HuggingFacePipeline' class  
my_llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

#creating an object of class 'ChatHuggingFace' with defined model
model = ChatHuggingFace(llm = my_llm)

#calling 'invoke' method for query
result = model.invoke("What are the characteristics of cat?")

#printing output
print(result.content)