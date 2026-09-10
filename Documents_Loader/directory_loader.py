from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

result=loader.lazy_load()


for ducument in result:
    print(ducument.metadata)

