class EmptyPerson:
    pass


print(EmptyPerson)
print(EmptyPerson())


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name  # private with __
        self.last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def walk(self):
        return f"{self.__first_name} is walking."


helder = Person("Helder", "D.O.")
print(helder)
print(f"{helder.get_first_name} {helder.last_name}")
print(helder.walk())
helder.__first_name = "John"
print(helder.walk())
helder.set_first_name("John")
print(helder.walk())
