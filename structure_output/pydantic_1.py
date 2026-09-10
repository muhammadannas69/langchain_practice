from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Student(BaseModel):
    
    name:str="annas"
    age : Optional[int]=None
    email:EmailStr
    cgpa: float = Field(gt=0,lt=10,default=1)
    
new_student = {'email':"anb@gmail.com"}

student = Student(**new_student)


print(student)