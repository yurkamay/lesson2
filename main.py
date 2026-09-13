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
class item():
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





