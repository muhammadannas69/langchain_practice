from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

loader = CSVLoader(file_path='student_data.csv')

data = loader.load()

print(data[0])