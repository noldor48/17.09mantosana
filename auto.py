class Vehicle:
        def __init__(self, make, model, year, price):
            self.make = make
            self.model = model
            self.year = year
            self.price = price
        def display_info(self):
              print(f"Make: {self.make},Model: {self.model},Year: {self.year},Price: {self.price}")

class Car(Vehicle):
        def __init__(self, make, model, year, price, num_doors, body_style):
            super().__init__(make, model, year, price) 
            self.num_doors = num_doors
            self.body_style = body_style
        def display_info(self):
            print(f"Make: {self.make},Model: {self.model},Year: {self.year},Price: {self.price},body_style: {self.body_style},num_doors: {self.num_doors}")   

class Truck(Vehicle):
        def __init__(self, make, model, year, price, bed_lenght, towing_capasity):
            super().__init__(make, model, year, price) 
            self.bed_lenght = bed_lenght
            self.towing_capasity = towing_capasity
        def display_info(self):
            print(f"Make: {self.make},Model: {self.model},Year: {self.year},Price: {self.price},bed_lenght: {self.bed_lenght},towing_capasity: {self.towing_capasity}")  
a=Vehicle("ko?","top","1488","shawel",)
a.display_info()
c=Car("ko?","top","1488","shawel","4","nice")
c.display_info()
t=Car("ko?","top","1488","shawel","6m","much")
t.display_info()