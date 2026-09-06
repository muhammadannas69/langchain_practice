from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)


class Person(BaseModel):
    name:str = Field(description="name of the person")
    age:int=Field(gt=18,description="age of the person")
    city:str=Field(description="name of the city the person belong too")
    
parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template='generate the name ,age and city of fictional {place} person \n {format_instructions}',
    input_variables=["place"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = template | model| parser

final=chain.invoke({'place':'pakistan'})


print(final)