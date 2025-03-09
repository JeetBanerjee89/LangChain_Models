#importing libraries
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

#fetching API key
load_dotenv()

#creating an object of class 'ChatAnthropic' with defined model 
model = ChatAnthropic(model = 'claude-3-7-sonnet-20250219')

#calling 'invoke' method for query
result = model.invoke('Bangalore is famous for what?')

#printing output
print(result.content)