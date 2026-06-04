from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

document = [
    "Hello world",
    "This is a test document.",
    "LangChain is great for building applications with LLMs."
]

result = embedding.embed_documents(document)

print(str(result))