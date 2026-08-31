from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text ="""class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
# Creating objects
student1 = Student("Ali", 20, 85)
student2 = Student("Ahmed", 21, 45)

# Using object methods
student1.display_info()"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 350,
    chunk_overlap=0,
)

result=splitter.split_text(text)

print(len(result))

print(result)