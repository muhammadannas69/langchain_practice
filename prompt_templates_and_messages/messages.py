from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

messages = [
    SystemMessage(content="your are ai tutor"),
    HumanMessage(content="tell me about Ai")
]

result = model.invoke(messages)
print(result.text)