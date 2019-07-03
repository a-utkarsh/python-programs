class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving maxspeed ' + str(self.__maxspeed))
    def setspeed(self, speed):
        self.__maxspeed =speed
        print(self.__maxspeed)



redcar = Car()

redcar.drive()
redcar.setspeed(320)
redcar.drive()
redcar._Car__maxspeed = 10 # will change variable because its private
redcar.drive()
