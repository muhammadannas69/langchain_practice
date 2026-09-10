from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

parsers = StrOutputParser()


prompt1 = PromptTemplate(
    template='Create a simple joke on {topic}. Return only the joke in plain text. Do not use Markdown or special formatting.',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Explain the following in simple plain text. Do not use Markdown, bold, headings, or special formatting.\n{text}',
    input_variables=['text']
)


chain = prompt1|model|parsers

parallal_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'expalanation':prompt2|model|parsers
})


final_chain = chain|parallal_chain

print(final_chain.invoke({'topic':'football'}))