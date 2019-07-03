class Parent():
    def __init__(self, last_name, eye_colour):
        self.ln= last_name
        self.ec= eye_colour

    def show_info(self):
        print(self.ln+ "eye_colour is" + self.ec)

class Child(Parent):
    def __init__(self,last_name, eye_colour , no_of_toys):
        self.no_toys = no_of_toys
        Parent.__init__(self, last_name, eye_colour)
    def show_info(self):
        print(self.ln+ "eye_colour is" + self.ec + "no of toys are" + str(self.no_toys))
Avinash = Parent("Shetty", "Brown")
Rahul = Child("Shetty", "Black",5)
Avinash.show_info()
Rahul.show_info()


