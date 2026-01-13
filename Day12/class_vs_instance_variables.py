class Dog:
    species = "Canine"
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")
print(dog.species, dog.name)