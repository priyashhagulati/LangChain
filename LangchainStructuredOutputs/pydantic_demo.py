from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'nitish' # default value is 'nitish', if we don't provide any value for name, it will take the default value
    age: Optional[int] = None # age is optional, if we don't provide any value for age, it will take the default value of None
    email: EmailStr 
    cgpa: float = Field(gt = 0, lt = 10, default = 5, description = "Cumulative Grade Point Average") # cgpa should be greater than 0 and less than 10
 
new_student = {'name': 'Bob', 'age': '32', 'email': 'abc@gmail.com', 'cgpa': '8.5'} #error if we put 32 instead of 'Bob' -> Input should be a valid string

#'age': '32' -> type coercing

student = Student(**new_student)

student_dict = dict(student) # convert pydantic model to dictionary

print(student_dict['age' ])

student_json = student.model_dump_json() # convert pydantic model to json

print(student_json)