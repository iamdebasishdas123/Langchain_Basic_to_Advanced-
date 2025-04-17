from langchain_openai import OpenAI

# API Key Loader
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct",max_tokens=20)

results=llm.invoke("Who is the Prime innister of india?")

print(results)