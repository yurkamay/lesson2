class Human:
    def __init__(self, name):
        self.name = name

class Auto():
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, *args):
        for person in args:
            self.passengers.append(person)
h1 = Human("John")
h2 = Human("Jane")
car1 = Auto("Bmw")
car1.add_passenger(h1,h2)
print (car1.passengers)
print(car1)




