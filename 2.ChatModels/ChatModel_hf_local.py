from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline  #main module to call the openai api
#import os

#os.environ['HF_HOME'] ='D:/huggingface_cache' #set the environment variable to the current working directory

llm=HuggingFacePipeline.from_model_id(model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',task='text-generation',
                                      pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100))


model=ChatHuggingFace(llm=llm)

result=model.invoke('What is the capital of india?') #Translate the following text to French: Hello, how are you? invoke the model with the text to translate to French


print(result.content)