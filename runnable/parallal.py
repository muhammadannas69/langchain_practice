from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

parsers = StrOutputParser()


prompt1 = PromptTemplate(
    template="creta a tweeter post {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="creta a linkedin post {topic}",
    input_variables=['topic']
)


parallal_chain = RunnableParallel({
    'tweeter':prompt1|model|parsers,
    'linkedin':prompt2|model|parsers
})

result = parallal_chain.invoke({'topic':'football'})


print(result)