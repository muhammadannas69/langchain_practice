from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


loader = WebBaseLoader(url)

docs = loader.load()

parser = StrOutputParser()



prompt = PromptTemplate(
    template='Answers the following question \n {question}\n from the following text \n {text}',
    input_variables=['question','text']
)


chain = prompt | model | parser

result = chain.invoke({'question':'explain in 5 line','text':docs[0].page_content})

print(result)