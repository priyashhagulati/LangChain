from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text = "Hello world"

vector = embedding.embed_query(text)

print(str(vector))

document = [
    "Hello world",
    "This is a test document.",
    "LangChain is great for building applications with LLMs."   ]

vectors = embedding.embed_documents(document)

print(str(vectors))