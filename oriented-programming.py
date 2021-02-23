# OBJECTS
print(type(1))
print(type('A'))
print(type([]))
print(type(()))
print(type({}))

"""
Output:
<class 'int'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
"""

# CLASS
# Create a new object type called Sample
class Sample:
    pass

# Instance of Sample
x = Sample()
print(type(x))

"""
Output:
<class '__main__.Sample'>
"""


# ATTRIBUTES
class Dog:
    def __init__(self, breed):
        self.breed = breed

kembot = Dog(breed='Lab')
kimchi = Dog(breed='Huskie')
hb = Dog(breed='Frenchie')
titan = Dog(breed='Local')
lucky = Dog(breed='Askal')

print(kembot.breed)
print(kimchi.breed)
print(hb.breed)
print(titan.breed)
print(lucky.breed)

"""
Output:
Lab
Huskie
Frenchie
Local
Askal
"""

class Dog_Second:
    # Class Object Attribute
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


dog_info = Dog_Second('Lab', 'Kembot')
print(dog_info.species)
print(dog_info.breed)
print(dog_info.name)

"""
Output:
Mammal
Lab
Kembot
"""

class Dog_Third:
    # Class Object Attribute
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print("WOOF! My name is {}, my breed is {}, my number is {}".format(self.name, self.breed, number))


dog_info = Dog_Third('Lab', 'Kembot')
print(dog_info.bark(11111111))

"""
Output:
WOOF! My name is Kembot, my breed is Lab, my number is 11111111
"""


# METHODS
class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

"""
Output:
Radius is:  1
Area is:  3.14
Circumference is:  6.28
"""

c.setRadius(2)
print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

"""
Output:
Radius is:  2
Area is:  12.56
Circumference is:  12.56
"""

# INHERITANCE
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()

"""
Output:
Animal created
Dog created
"""

d.whoAmI()
d.eat()
d.bark()

"""
Output:
Dog
Eating
Woof!
"""

# POLYMORPHISM
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'

barney = Dog('Barney')
tom = Cat('Tom')

print(barney.speak())
print(tom.speak())

"""
Output:
Barney says Woof!
Tom says Meow!
"""

for pet in [barney, tom]:
    print(pet.speak())

"""
Output:
Barney says Woof!
Tom says Meow!
"""

def pet_speak(pet):
    print(pet.speak())

pet_speak(barney)
pet_speak(tom)

"""
Output:
Barney says Woof!
Tom says Meow!
"""

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):

    def speak(self):
        return self.name + ' says Woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says Meow!'


barney = Dog('Barney')
tom = Cat('Tom')

print(barney.speak())
print(tom.speak())

"""
Output:
Barney says Woof!
Tom says Meow!
"""

# SPECIAL METHODS
# The __init__(), __str__(), __len__() and __del__() special methods
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is deleted")


book = Book("Python - Smarter not Harder", "Al Ardosa", 100)

print(book)
print(len(book))
del book

"""
Output:
A book is created
Title: Python - Smarter not Harder, author: Al Ardosa, pages: 100
100
A book is deleted
"""