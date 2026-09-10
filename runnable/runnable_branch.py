from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnablePassthrough,RunnableParallel,RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a detail report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summerize the following text \n {text}',
    input_variables=['text']
)


chain = prompt|model|parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>50,prompt2|model|parser),
    RunnablePassthrough()
)

final_chain = chain|branch_chain


print(final_chain.invoke({"topic":"football"}))





