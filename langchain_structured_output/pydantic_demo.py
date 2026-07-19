from pydantic import BaseModel

class Student(BaseModel):

    name : str



#new_student_w = {'name': 29}
#student_w = Student(** new_student_w)
#print(student_w)

new_student = {'name': 'Balram'}
student = Student(** new_student)
print(student)
print(student.name)
