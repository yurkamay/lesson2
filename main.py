'''class Human:
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
print(car1)'''

'''def create_html_tag(tag, *content, **attributes):
   attribute_list = [f'{key}="{value}"' for key, value in attributes.items()]
   attribute_string = " " + " ".join(attribute_list) if attribute_list else ""
   return f'<{tag}{attribute_string}>{content}</{tag}>'''''
'''class item():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class warehouse():
    def __init__(self):
        self.inventory = []

    def add_item(self, *args):
            for item in args:
                self.inventory.append(item)

    def total_weight(self):
         total_weight = 0
         for item in self.inventory:
            total_weight += item.weight
         print(f"pfu dfuf{total_weight}")
wh1 = warehouse()
it1 = item("Apple", 100)
it2 = item("Orange", 200)
wh1.add_item(it1,it2)
wh1.total_weight()
print(wh1.inventory)
class Employee():
    company = "Techcor"
    def work(self):
        print("I am working")
class Developer(Employee):
    language = "Python"
    def work(self):
        print("I write code")
dev = Developer()
print(dev.company)
dev.work()'''
'''class Character():
    def __init__(self, health = 100):
        self.health = health
    def attack(self):
        print("Базова атака")
class Warrior(Character):
    def __init__(self, health = 150):
        self.health = health
class mage(Character):
    def __init__(self, health = 100):

        self.health = health

    def attack(self):
        print("атака магією")

c1 = Character()
w1 = Warrior()
m1 = mage()
print(c1.health)
print(w1.health)
print(m1.health)
m1.attack()
w1.attack()'''
'''class Account():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposite(self,ammount):
        if ammount > 0:
            self.__balance += ammount
        else:
            print("Cevf vf' ,enb ,skmij. pf 0")
acc = Account(balance=1000)
print(acc.get_balance())
acc.deposite(100)
print(acc.get_balance())'''
'''class user():
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    def check_password(self, password):
        password1 = int(input("Please enter your password: "))

        if password1 == self.__password:
            print("True")
        else:
            print("False")
u1 = user("John", 1234)
u1.check_password("")'''
'''class Shape():
    def __init__(self, color):
        self.color = color
class rectangle(Shape):
    def __init__(self, color ,width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
s1 = Shape("red")
r1 = rectangle(color = "blue", width = 100, height = 100)
print(r1.area())'''
class Document():
    pass
class Image():
    pass
d1 = Document()
i1 = Image()
d2 = Document()
files = ( d1, i1, d2, 42)
for item in files:
    if isinstance(item,Document):
        print("це документ")
    else :
        print("Не документ")
