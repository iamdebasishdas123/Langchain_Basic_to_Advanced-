from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Define the model

model= ChatGroq(model="llama-3.1-8b-instant")

# Prompt for model 

prompt=PromptTemplate(template="Give me 5 line summary of thr {topic}", input_variables=["topic"])

# Output parser
parser=StrOutputParser()

# Chains

chain= prompt | model | parser

resluts=chain.invoke({"topic":"Grobal Warming"})

# Print summary
print(resluts)


# Pipeline Printing

chain.get_graph().print_ascii()