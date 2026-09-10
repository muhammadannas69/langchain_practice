from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

sample ="""Python is a popular programming language used for web development, automation, data analysis, and software development. It is known for its simple syntax and readability.

The solar system consists of the Sun and the objects that orbit it. There are eight planets, and Earth is the third planet from the Sun. The Moon is Earth's natural satellite.

Football is a popular sport played between two teams. Each team tries to score goals by moving the ball into the opponent's goal. Players use passing, shooting, and defending skills."""

splitter = SemanticChunker(
    model,breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

result= splitter.create_documents([sample])

print(result)

print("length",len(result))

