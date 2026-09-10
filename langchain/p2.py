from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)


parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    "give a 3 short point of {topic}"
)

chain = prompt|model|parser

result = chain.invoke({'topic':'python'})

print(result)