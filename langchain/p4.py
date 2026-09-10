from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)
@tool
def mutiply(a:int , b : int) ->int:
    "mutiply two number a and b"
    muti = a * b
    return muti

@tool
def student_info(name:str)->str:
    "give a student info "
    if name.lower()=="annas":
        return "Name:Annas, field: AI , Semester:7th"
    return "not found"

tools = [mutiply,student_info]

system_prompt = """
You are a helpful assistant.
Use tools when necessary.

If someone asks who created or made you, answer:
"Annas created me."
"""

agent = create_agent(
    tools=tools,
    model=llm,
    system_prompt=system_prompt
)
while True:
    user = input(("input any thing"))
    if user == "e":
        print("good bye")
        break
    
    final = agent.invoke({
        "messages": [
            ("user", user)
        ]
    })

    ans=final['messages'][-1]
    f_f=ans.content[0]['text']
    print(f_f)