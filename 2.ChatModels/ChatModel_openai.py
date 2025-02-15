from langchain import chatopenai #import the ChatModel class from langchain module
from dotenv import load_dotenv #to load the environment variables fro .env file


load_dotenv() #load the environment variables from .env file

model =chatopenai(model='gpt-4',temperature=1.5,max_completion_tokens=10) #initialize the openai model

result=model.invoke('What is the capital of india?') #invoke the model with the text to translate to French

print(result.content) #print the result