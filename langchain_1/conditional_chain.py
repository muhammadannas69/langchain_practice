from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_xai import ChatXAI
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal


load_dotenv()


model1 = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

class FeedBack(BaseModel):
    
    sentiment:Literal['positive','nagetive']=Field(description="give a sentiment of the feedback")

parser = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object=FeedBack)

prompt = PromptTemplate (
    template="Classify the sentiment of the following text into positive or negative \n {feedback} \n {format_instruction}",
    
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)






classifier_chain = prompt | model1 | parser2



prompt2 = PromptTemplate(
    template='write an appropriate respones to  this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='write an appropriate respones to  this nagetive feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',  prompt2 | model1 | parser),
    (lambda x:x.sentiment == 'nagetive',  prompt3 | model1 | parser),
    RunnableLambda(lambda x: "could not find sentiments")
)

chain = classifier_chain | branch_chain


# print(chain.invoke({'feedback':"this is trible phone"}))

chain.get_graph().print_ascii()