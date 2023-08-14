
class Char:

    def __init__(self, name, age):
        if not name.isalpha() or not str(age).isdigit():
            raise "Only letters allowed in name and digits in age"
        elif age > 120 or age < 0:
            raise "Age value should be between 0 and 120."
        else:
            self.__name = name
            self.__age = age

    def nick_change(self, new):
        self.__name = new

    def youth_potion(self, years):
        self.__age = years

    def print_char(self):
        print(f"{self.__name}, {self.__age}")

ch1 = Char("Gilbert", 42)
ch2 = Char("Fred", 12)
ch3 = Char("Petro", 121)
ch1.nick_change("Vasya")

ch1.print_char()
