from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal,Optional

load_dotenv()

model = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

## 1.PromptTemplate
prompt=PromptTemplate(template="tell me about {topic} and give a message to {object}",
                      input_variables=["topic", "object"])


## 2.typedict
class review(TypedDict):
    
    topic :Annotated[list[str],'tell me name of the topic']
    object: Annotated[list[str], "Tell me name of the object"]
    message: Annotated[str, "tell me 5 line of the message"]
    name : Optional[str] =None
    review: Literal['positive', 'negative','nutral']

model=model.with_structured_output(review)


## 3. Chain 


## 4. Other Method 
prompt=prompt.invoke({'topic':"Gobal Warmings", 'object':"Humans"})

response=model.invoke(prompt)

## 5. Result

print(response)

print(response["review"])
print(response["name"])
