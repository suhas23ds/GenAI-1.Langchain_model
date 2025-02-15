from langchain_openai import openai  #main module to call the openai api
from dotenv import load_dotenv #to load the environment variables fro .env file

load_dotenv() #load the environment variables from .env file

llms=openai(model='gpt-3.5-turbo-instruct') #initialize the openai model

result = llms.invoke('What is the capital of india?') #Translate the following text to French: Hello, how are you? invoke the model with the text to translate to French


print(result)