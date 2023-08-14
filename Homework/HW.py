'''Напишіть клас "Person", який має властивості name (ім'я) і age (вік). ' \
Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу. ' \
Забезпечте методи для доступу до цих властивостей та встановлення їх значень.'''


class Char:

    def __init__(self, name, age):
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
ch1.nick_change("Vasya")

ch1.print_char()
