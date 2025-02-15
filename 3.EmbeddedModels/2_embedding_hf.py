from langchain_huggingface import HuggingFaceEmbeddings  # Import the HuggingFaceEmbeddings class

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')  # Create an instance of the HuggingFaceEmbeddings class

text='Delhi is the capital of India'  # Define the text to be embedded

result=embedding.embed_query(text)  # Embed the text

print(str(result))  # Print the result