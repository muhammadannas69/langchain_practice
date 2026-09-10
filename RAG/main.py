from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests

load_dotenv()

@tool
def mutiply(a:int , b:int) -> int:
  """Given 2 number a and b this tool returns product"""
  return a*b

mutiply.name

mutiply.description

mutiply.args

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

query = HumanMessage('can you mutiply 3 with 100')

messages = [query]

llm_with_tools=llm.bind_tools([mutiply])

result=llm_with_tools.invoke(messages)

messages.append(result)

result.tool_calls[0]['args']

tool_message=mutiply.invoke(result.tool_calls[0])

messages.append(tool_message)

messages

final=llm_with_tools.invoke(messages)

print(final.text)
