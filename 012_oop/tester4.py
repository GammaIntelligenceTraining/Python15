class Car:

    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def make(self):
        return self.__make

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @color.deleter
    def color(self):
        self.__color = None


car1 = Car('Honda', 'Civic', 'black')

print(car1.color)
car1.color = 'red'
del car1.color
print(car1.__dict__)