from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('text_splitter_practice.pdf')

docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 5,
    separator= ""
)


result=splitter.split_documents(docs)

print(result[0])