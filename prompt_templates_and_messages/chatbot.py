from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)



chat_history = [
    SystemMessage(content="your a teacher")
]



print("="*30)
print("Chatbot")
print("="*30)



while True:
    # print("for exit enter e")
    user = input("You: ")
    chat_history.append(HumanMessage(content=user))
    
    if user == "e":
        print("AI: Good bye")
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.text)