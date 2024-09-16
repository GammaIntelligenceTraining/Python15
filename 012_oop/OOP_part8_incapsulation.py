# Incapsulation
class Car:

    def __init__(self, make, model, color):
        self.make = make
        self._model = model
        self.__color = color


bmw = Car('BMW', 'M5', 'red')

# Regular attribute accessible from everywhere
print(bmw.make)
# Attribute accessible from everywhere but meant to be used inside class
print(bmw._model)
# Attribute accessible from class only, still can be accessed by `_Classname_attribute`
print(bmw._Car__color)
