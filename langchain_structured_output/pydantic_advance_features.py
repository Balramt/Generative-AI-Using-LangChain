from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str = 'Balram'
    age: Optional[int] = None
    mobile: int
    email: EmailStr
    cgpa: float = Field(gt=0, lt= 10, default=5, description= 'A decimal value representation')



new_student = {'age': 32, 'mobile': '9911258164', 'email': 'abc@gmial.com'} #Here we saw the coerce behaviour of pydantic beacuse we pass string as mobile but due to mobile defined as integer auto type conversion takes place but can not pass abc as mobile number then it is error 
student = Student(** new_student)
print(student)
print(student.name)


student_dict = dict(student)
print(student_dict['age'])


student_json = student.model_dump_json()
print(student_json)
