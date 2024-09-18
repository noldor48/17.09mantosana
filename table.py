class Table:
    def __init__(self, l, w, h):
        self.lenght = l
        self.width = w
        self.height = h
        if isinstance(self, KitchenTable):
            p =int(input("Cik vietu: "))
            self.places = p
    def info(self):
        print(f"Garums ir {self.lenght}, platums ir: {self.width}, augstums ir: {self.height}")

class DeskTable(Table):
    def square(self):
        return self.width * self.lenght

class ComputerTable(Table):
    def square(self, monitor=0.0):
        return self.width * self.lenght - monitor

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        super().__init__(l, w,h)
 #       Table.__init__(self, l, w, h)
        self.places = p

t1 = Table(1,2,3)
t1.info()
t2 = DeskTable(3,5,6)
print(t2.square())
t2.info()
t3 = ComputerTable(7,5,6)
print(t3.square())
t3.info()
t4 = KitchenTable(45,65,76,5)

t4.info()