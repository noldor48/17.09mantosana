class Pupil:
    _age=0 #protected
    __age=0 #privat
    age=0 #public
    name="Janis"
    def say(self):
        print(pupil._age, pupil.__age, pupil.age)
        
pupil=Pupil()
pupil._age=-1
pupil.__age=-2
pupil.age=-3
pupil.say()
#print(dir(pupil))
