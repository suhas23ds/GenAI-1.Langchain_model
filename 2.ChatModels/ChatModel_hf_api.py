from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint  #main module to call the openai api
from dotenv import load_dotenv #to load the environment variables fro .env file

load_dotenv() #load the environment variables from .env file

llm=HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm) #initialize the openai model

result=model.invoke('What is the capital of india?') #Translate the following text to French: Hello, how are you? invoke the model with the text to translate to French

print(result.content)