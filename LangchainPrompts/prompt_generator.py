from langchain_core.prompts import PromptTemplate

#template
template = PromptTemplate(
    template = """Summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
input_variables=["paper_input", "style_input", "length_input"],
validate_template=True #default validation
)

template.save("template.json") #reusable

#serialized = dumps(template)

#with open("template.json", "w") as f:
#    f.write(serialized)

"""
Why prompt templates? Default validation, reusable, LangChain Ecosystem
"""