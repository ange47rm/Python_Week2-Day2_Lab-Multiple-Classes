class Person():

    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination

    def person_gets_on_bus (self, bus):
        if self.destination == bus.destination:
            return True