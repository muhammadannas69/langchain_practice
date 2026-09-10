from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text ="""# Artificial Intelligence

Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that normally require human intelligence.

## Machine Learning

Machine Learning (ML) allows computers to learn patterns from data and make predictions.

### Types of ML

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

## Natural Language Processing

NLP enables computers to understand and process human language. It is used in chatbots, translation, and text classification.

## LangChain

LangChain is a framework for building applications with Large Language Models.

It provides components such as:

- Document Loaders
- Text Splitters
- Prompt Templates
- Output Parsers"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 350,
    chunk_overlap=0,
)

result=splitter.split_text(text)

print(len(result))

print(result[0]) 