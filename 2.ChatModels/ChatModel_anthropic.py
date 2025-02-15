from langchain_anthropic import chatanthropic
from dotenv import load_dotenv

load_dotenv()

model=chatanthropic(model='claude-3-5-sonnet-20241022',temperature=1.5,max_completion_tokens=10)



result =model.invoke('What is the capital of india?') #invoke the model with the text to translate to French

print(result.content) #print the result