from typing import TypedDict


class Person(TypedDict):

    name: str
    age: int

new_person: Person = {"name": "Balram", "age":30}


print(new_person)