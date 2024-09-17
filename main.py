class Geom:
    name="Geom"

class Line(Geom):
    def draf(self):
        print("Linijas zimesana")

g=Genom()
l=Line()
l.draw()
print(l.name)