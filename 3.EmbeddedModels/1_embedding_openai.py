from langchain_openai import OpenAIEmbeddings  # Import the OpenAIEmbeddings class
from dotenv import load_dotenv  # Import the load_dotenv function

load_dotenv()  # Load the environment variables from the .env file

embedding=OpenAIEmbeddings(model='text-embedding-3-large')  # Create an instance of the OpenAIEmbeddings class

result=embedding.embed_text('Delhi is the capital of India',dimension=32)  # Embed the text

print(str(result))  # Print the result