from dataclasses import dataclass, astuple


@dataclass
class Person:
    name: str
    age: int

    # def __getitem__(self, item):
    #     if item == 0:
    #         return self.name


people = [
    Person("Daniel", 52),
    Person("Jose", 51),
]
