from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=1.5, max_completion_tokens=10)


result = model.invoke('What is the capital of india?') #invoke the model with the text to translate to French

print(result.content) #print the result