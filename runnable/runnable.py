from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    temperature = 0
)


def word_count(text):
    return len(text.split())

parsers = StrOutputParser()
passthrough=RunnablePassthrough()
prompt = PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)

chain = prompt | model | parsers

parallal_chain = RunnableParallel({
    'joke':passthrough,
    'word_count':RunnableLambda(word_count) 
}) 

final_chain = chain|parallal_chain

result=final_chain.invoke({'topic':'football'})


final_result= """{} \nword count {}""".format(result['joke'],result['word_count'])

print(final_result)