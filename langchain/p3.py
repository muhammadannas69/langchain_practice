from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()


parser = StrOutputParser()

document = TextLoader("data.txt")
text = document.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size = 600,
    chunk_overlap = 20
)
chunks = spliter.split_documents(text)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vectorstore = FAISS.from_documents(
    chunks,
    embedding
)

documents = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


prompt = PromptTemplate.from_template(
    """
Answer the question using only the context below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
I don't know based on the provided context.
"""
)



def format_docs(documents):
    context = "\n".join(doc.page_content for doc in documents)
    return context


parallal_chain = RunnableParallel({
    "context": documents|RunnableLambda(format_docs),
    "question":RunnablePassthrough()
})


chain = parallal_chain|prompt|model|parser
intial = "what is python"

final = chain.invoke("what is python")
     
print(final)