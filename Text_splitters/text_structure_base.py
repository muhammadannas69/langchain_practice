from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating systems that can perform tasks that normally require human intelligence. These tasks include understanding language, recognizing patterns, making decisions, solving problems, and learning from experience.

Machine Learning (ML) is a subset of Artificial Intelligence. Instead of explicitly programming a computer to perform every task, machine learning allows a system to learn patterns from data. There are several common types of machine learning, including supervised learning, unsupervised learning, and reinforcement learning.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)