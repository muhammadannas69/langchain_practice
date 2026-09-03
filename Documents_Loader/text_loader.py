from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

parser = StrOutputParser()

loader = TextLoader('text.txt',encoding='utf-8')

prompt = PromptTemplate(
    template='Explain the {topic}',
    input_variables=['topic']
)

docs = loader.load()


chain = prompt|model|parser
print(chain.invoke({'topic':docs[0].page_content}))

