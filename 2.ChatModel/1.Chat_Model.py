from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


# 3 Importent parameters for models 
# 1. model: The model name to use. For example, "gpt-3.5-turbo" or "gpt-4".
# 2. temperature: Controls the randomness of the output. Lower values make the output more deterministic, while higher values make it more random.
# 3. max_tokens: The maximum number of tokens to generate in the response.

model=ChatOpenAI(model="gpt-4", temperature=0.5, max_tokens=50)

results=model.invoke("What is Capital of the India?")

print(results)

print(results.content)