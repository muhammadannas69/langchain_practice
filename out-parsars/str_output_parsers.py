# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text_generation"
# )


# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)


template1 = PromptTemplate(
    template="write a detail on {topic}",
    input_variables=["topic"]
)


template2 = PromptTemplate(
    template="write a 5 line summary on the following text. \n {text}",
    input_variables=["text"]
)

# prompt1=template1.invoke({'topic':'Black hole'})

# result= model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# final_result = model.invoke(prompt2)
parsars = StrOutputParser()

chain = template1 |model | parsars | template2 | model | parsars
result=chain.invoke({'topic':"black hole"})
print(result.text)
