class Geom:
    name="Geom"

class Line(Geom):
    def draw(self):
        print("Linijas zimesana")
    def set_cords(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        print(x1, y1, x2, y2)
g=Geom()
l=Line()
l.draw()
l.set_cords(1,4,5,7)
print(l.name)