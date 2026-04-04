
#Task 1 Basic Class and Object Creation. #Task2 Construction and Encapsulation

class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price
        self.category=category
    
    def get_info(self):
        print(f"the product details are  {self.name}  {self.__price},{self.category}")

    def get_price(self):
        print(f" The price of the product is {self.__price}")

    def set_price(self,new_price):
        if new_price >0:
            self.__price=new_price

    

p=Product("Lalit",123,"human")
p.get_info()
p.get_price()
p.set_price(100)
p.get_price()

print(len("python"))


#Task 3 Inheritance
class ElectornicProducts(Product):
    def __init__(self,name,price,category,warranty_year):
        super().__init__(name,price, category)
        self.warranty_year=warranty_year

    def get_info(self):
        print(f"the warrent years of ElectonicProducts is ${self.warranty_year} ")

ep=ElectornicProducts("suraj" ,230 , "human" ,27)

ep.get_info()



#Task4 Polymorphism

class Laptop(Product):
    pass

class Mobile(Product):
    pass


import numpy as np


three=np.array([
    [
        [4,5],
        [7,9]
    ],
    [
        [34,5],
        [5,6]
    ]
])
print(three)
print(three.ndim)

import numpy as np
import numpy as np

four = np.array([
    [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
    ]
])
print(four)
print(four.ndim)
print(four.itemsize)


print(np.arange(16))


class Laptop(Product):
    def __init__(self,name,price,category,style):
        super().__init__(name,price,category)
        self.style=style

    def get_info(self):
        print(f"the style is ${self.style}")


class Mobile(Product):
    def __init__(self,name,price,category,style):
        super().__init__(name,price,category)
        self.style=style

    def get_info(self):
        print(f"the style is ${self.style}")


lp1=Laptop("suraj" ,230 , "human" ,"yoboy")
lp2=Laptop("lalit" ,230 , "human" ,"yoboy22")

mb1=Mobile("apple" ,230 , "fruit" ,"yoboyytyui")
mb2=Mobile("ball" ,230 , "fruit" ,"uhggggg")


products=[lp1,lp2,mb1,mb2]

for product in products:
    print(product.get_info())


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self,amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"the amount of CreditCardPayment {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"the amount is UPIPayment {amount}")


c= CreditCardPayment()
u=UPIPayment()

c.process_payment(5000)
u.process_payment(6000)

arry_three=np.array([
    [
        [5,6],
        [8,0],
    ],
    [
        [1,3],
        [4,2],
    ]
])
print(arry_three.ndim)
print(arry_three[1,1,0])



