from  langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant")

# Define the prompts
prompt1=PromptTemplate(template="Can U tell me the future of {job_role} in this sector and tell about pro and cons", input_variables=["job_role"]
                       )

prompt2=PromptTemplate(template="Can U tell me the current Job market trends for {job_role}", input_variables=["job_role"]
                       )
prompt3=PromptTemplate(template="Analysing the {future} and {market_trend} this job role good for me or not",input_variables=["future","market_trend"])

# Define the output parsers

parser=StrOutputParser()

# Create Parallel pipe line

sequence=RunnableParallel({
    "future": prompt1 | model | parser,
   "market_trend": prompt2| model | parser}
)

# Define the final prompt
main= prompt3 | model | parser

# Test the pipeline
chain= sequence | main | parser

results=chain.invoke({"job_role": "Data Science"})

print(results)

chain.get_graph().print_ascii()

