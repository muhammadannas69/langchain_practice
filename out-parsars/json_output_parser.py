from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser



load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text_generation"
# )
# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="write the name,age and city of a fictional person \n {format_instraction}",
    input_variables=[],
    partial_variables={"format_instraction":parser.get_format_instructions()}
)

chain = template|model|parser

result = chain.invoke({})


print(result)