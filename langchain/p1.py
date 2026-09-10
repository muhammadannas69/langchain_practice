from langchain_core.runnables import RunnableLambda

run = RunnableLambda(lambda x : x * 2)

result = run.invoke(5)

print(result)