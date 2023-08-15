class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def animal_info(self):
        print(f'{self.name}, {self.species}')


class Mammal(Animal):

    def __init__(self, name, species, nutrition_type):
        super().__init__(name, species)
        self.nutrition_type = nutrition_type

    def animal_info(self):
        print(f'{self.name}, {self.species}, {self.nutrition_type}')


class Carnivore(Mammal):

    def __init__(self, name, species,
                 nutrition_type,
                 teeth_count):
        super().__init__(name, species, nutrition_type)
        self.teeth_count = teeth_count

    def animal_info(self):
        print(f'{self.name}, {self.species}, {self.nutrition_type}, {self.teeth_count}')


class Lion(Carnivore):

    def __init__(self, name, species,
                 nutrition_type,
                 teeth_count,
                 mane_size
                 ):
        super().__init__(name, species, nutrition_type, teeth_count)
        self.mane_size = mane_size

    def animal_info(self):
        print(f'{self.name}, {self.species}, {self.nutrition_type}, {self.teeth_count},{self.mane_size}')


lion = Lion("Lion Joe", "The cat", "Meat", "a lot of teeth", "Middle Lion's mane")
lion.animal_info()

otter = Carnivore("Otter Kel", "Otterries?", "Fish Meat", "Not that much as lion have")
otter.animal_info()

capybara = Mammal("Capy Frank", "Definitely Capybaras", "Veggies")
capybara.animal_info()