class Geom:
    name="Geom"
    def set_cords(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        print(x1, y1, x2, y2)
class Line(Geom):
    name="Line"
    def draw(self):
        print("Linijas zimesana")

class Rect(Geom):
    def draw(self):
        print("Rect zimesana")   
g=Geom()
l=Line()
r=Rect()
l.set_cords(1,4,5,7)
r.set_cords(2,4,5,7)
l.draw()
print(l.name)
r.draw()
print(r.name)
print(l.__dict__)
print(r.__dict__)