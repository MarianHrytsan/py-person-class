class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result_output = []
    for i, person in enumerate(people):
        result_output.append(Person(person["name"], person["age"]))
    for i, person in enumerate(people):
        if "wife" in person:
            for j in range(len(result_output)):
                if person["wife"] == result_output[j].name:
                    result_output[i].wife = result_output[j]
        elif "husband" in person:
            for j in range(len(result_output)):
                if person["husband"] == result_output[j].name:
                    result_output[i].husband = result_output[j]
    return result_output
