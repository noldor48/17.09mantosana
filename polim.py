class Pupil:
    __age=0

    def set_age(self, value:int):
        self.__age=value

pupil=Pupil()
pupil.__age=-1
print(pupil.__age)
#pupil.set_age()