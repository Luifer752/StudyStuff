from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, name, model):
        self.name = name
        self.model = model


    @abstractmethod
    def print_car(self):
        pass


class Sedan(Car):

    def __init__(self, name, model, doors):
        super().__init__(name, model)
        self.doors = doors

    def print_car(self):
        print(f"""This is {self.name} model: {self.model}, 
        there is {self.doors} doors.""")


class Suv(Car):

    def __init__(self, name, model, seats):
        super().__init__(name, model)
        self.seats = seats

    def print_car(self):
        print(f"""This is {self.name} model: {self.model}, 
        there is {self.seats} seats.""")


class SportCar(Car):

    def __init__(self, name, model, mspeed):
        super().__init__(name, model)
        self.mspeed = mspeed

    def print_car(self):
        print(f"""This is {self.name} model: {self.model}, 
        max speed is {self.mspeed}.""")


car1 = Sedan("WV", "Jetta", 4)
car2 = Suv("Toyota", "Tundra", 4)
car3 = SportCar("Pirozhok", "Classic", 80)

car1.print_car()
car2.print_car()
car3.print_car()