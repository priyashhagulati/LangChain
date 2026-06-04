from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.9) #temperature is a parameter that controls the randomness of the model's output. A higher temperature will result in more random outputs, while a lower temperature will make the output more deterministic.

result = model.invoke("What is the capital of France?")

print(result.content)  
