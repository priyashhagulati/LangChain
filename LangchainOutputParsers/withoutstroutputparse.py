from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.1-8B-Instruct',
    task = 'text-generation'    
)

model = ChatHuggingFace(llm=llm)

#1st Prompt -> detailed report
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}.',
    input_variables= ['topic']
)

#2nd prompt -> summary of the report 
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}.',
    input_variables= ['text']
)

prompt1 = template1.invoke({'topic': 'Blackhole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1})

result2 = model.invoke(prompt2)

print("Detailed Report: ", result1.content)
print("Summary: ", result2.content)