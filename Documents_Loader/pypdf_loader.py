from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

parser = StrOutputParser()

loader = PyPDFLoader('pypdf_practice.pdf')
docs=loader.load()

print(docs[0].page_content)
print(docs[0].metadata)