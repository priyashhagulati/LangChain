from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text \n {text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short question answers from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Understanding valuable insights from large datasets is important in making decisions in this fast-changing world, especially in data science and predictive applications. In detail, data scientists and analysts often aim to identify high-quality data candidates—free of missing values, duplicates, and inconsistencies—before aggregating datasets with diverse attributes for analysis. Taking housing price prediction as an example, in predicting housing prices, various factors come into play, including the location of the property (proximity to urban centers, crime rates), property characteristics (size, style, modernity), and regional policies (tax implications). With their domain-specific knowledge, analysts/scientists rank these attributes to inform the predictive utility function, which machine learning models then use to forecast housing prices.

Consider a scenario where a scientist must prioritize specific attributes over others based on their expertise. For example, an apartment in a central city like New York, with low crime rates, modern amenities, and high safety standards, might be favored over a historic house in a remote area. Even within similar urban settings, choices become complex—such as deciding between a centrally located apartment and a slightly less expensive one in a nearby suburb. Factors like neighborhood friendliness or environmental tranquility can also influence decision-making. Thus, making these variations in attribute importance are captured by a utility function, which quantifies the significance of each attribute in predicting outcomes like housing prices.

Traditional machine learning algorithms often require users to predefine their utility functions, which can be impractical or challenging for many users. The Blindly Optimal Data Discovery (BOD) and Predictive Learning Optimal Data Discovery (PLOD) algorithms [Hoang(2024a)] [Hoang(2024b)] address this by asking users to rank attributes and filtering datasets based on these rankings. But these approaches have limits in a way that may still result in subsets of data that do not perfectly align with the user’s intended utility function due to the lack of a precise match between the predicted and actual utility functions.

"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()
