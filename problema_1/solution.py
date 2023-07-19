from enum import Enum

class Gender(Enum):
    MALE = 0x0,
    FEMALE = 0x1,

class Person:
    def __init__(self, name: str, age: int, gender: Gender):
        self.name = name
        self.age = age
        self.gender = gender

class PersonList:
    def __init__(self):
        self.entries = []
        self.male_count = 0
        self.female_count = 0
        self.oldest = None
        self.youngest = None

    def append(self, person: Person):
        self.entries.append(person)

        if person.gender == Gender.MALE:
            self.male_count += 1
        else:
            self.female_count += 1

        if self.oldest is None or person.age > self.oldest.age:
            self.oldest = person

        if self.youngest is None or person.age < self.youngest.age:
            self.youngest = person

"""
Parse a PersonList from a list of comma-separated entries
"""
def parse_input(input: str) -> PersonList:
    list = PersonList()
    try:
        for line in input.splitlines():
            fields = line.split(",")
            name = fields[0]
            age = int(fields[1])
            gender = Gender.MALE if fields[2] == "male" else Gender.FEMALE

            person = Person(name, age, gender)
            list.append(person)
    except:
        raise ValueError("invalid input")

    print("Results:")
    print(f"{list.male_count} males, {list.female_count} females")
    print(f"oldest: {list.oldest.age}, youngest: {list.youngest.age}")

    return list

def test():
    input = ("John,11,male\n"
             "Mary,12,female\n"
             "Robert,32,male\n"
             )
    list = parse_input(input)
    assert list.youngest.name == "John"
    assert list.oldest.name == "Robert"
    assert list.male_count == 2
    assert list.female_count == 1

test()
