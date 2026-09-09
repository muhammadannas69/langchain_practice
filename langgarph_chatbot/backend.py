from langchain_google_genai import  ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=('gemini-3.5-flash')
)


class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]
    
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

def chat_node(state:ChatState):
    message = state['messages']
    system_message = SystemMessage(content="When asked who built you, reply: I am a chatbot of Annas.")
    responses = llm.invoke([system_message]+message)
    return {'messages':[responses]}


graph.add_node("chat_node",chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)