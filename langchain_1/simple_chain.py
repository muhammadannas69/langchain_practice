from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="generate 5 interesting fasts about {topic}",
    input_variables="topic"
)


model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

parser = StrOutputParser()


chain = prompt |model|parser

result= chain.invoke({"topic":"football"})

print(result)

chain.get_graph().print_ascii()