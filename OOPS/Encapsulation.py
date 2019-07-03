class Car:

   # def __init__(self):
    #    self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')


redcar = Car()
redcar.drive()
redcar._Car__updateSoftware()
#redcar._Car__updateSoftware()
#redcar._Car__updateSoftware()

'''The private attributes and methods are not really hidden, 

they’re renamed adding “_Car” in the beginning of their name.

The method can actually be called using redcar._Car__updateSoftware()'''