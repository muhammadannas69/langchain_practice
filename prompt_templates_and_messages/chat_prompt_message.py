from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage


chat_template = ChatPromptTemplate([
    ('system',"you are a helpful {domain} expart"),
    ('human',"Explain in simple tream, what is {topic}")
]
)

prompt = chat_template.invoke({'domain':"football","topic":"goal"})

print(prompt)