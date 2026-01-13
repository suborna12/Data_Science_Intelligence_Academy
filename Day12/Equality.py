class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id
        return False

