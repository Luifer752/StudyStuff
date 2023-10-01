class Shape:

    def __init__(self, colour):
        self.colour = colour

    def display_colour(self):
        print(f'{self.colour}')

class Rectangle(Shape):

    def __init__(self, colour, width, height):
        super().__init__(colour)
        self.width = width
        self.height = height

    def display_size(self):
        print(f'{self.width}, {self.height}')

    def display_colour(self):
        print(f'{self.colour}')


class Square(Rectangle):

    def __init__(self, colour, width, height, side_length):
        super().__init__(colour, width, height)
        self.side_length = side_length


    def display_size(self):
        print(f'{self.width}, {self.height}, {self.side_length}')

