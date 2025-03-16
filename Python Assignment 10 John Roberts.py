earth_pop = 6,000,000,000

'''This is the parent class of the following subclasses, or child classes. It has the colonization and spin methods within it.'''
class SolarObject:
    def __init__(self, name, distance, orbit_time):
        self.name= name
        self.distance = distance
        self.orbit = orbit_time

    def colonization(self):
        colonization = round((6000000000 / self.distance),2)
        print(self.name, "has a colonization score of", colonization)

    def spin(self):
        pass

'''The child class Planet takes the attributes and methods of SolarObject and adds in the details method, and adjusts
the method of 'spin' through polymorphism.'''

class Planet(SolarObject):
    def __init__(self, name, distance, orbit_time):
        super().__init__(name, distance, orbit_time)

    def spin(self):
        print(self.name, "spins slightly elliptical.")

    def details(self):
        print(self.name, "is", self.distance, "AU from the sun.")
        print(self.name, "takes", self.orbit, "days to orbit the sun.")

Earth = Planet("Earth", 1, 365)
Mars = Planet("Mars", 1.5, 687)

'''The child class Comet imports attributes from parent class SolarObject as well, with its own details and spin method
values through polymorphism.'''
class Comets(SolarObject):
    def __init__(self, name, distance, orbit_time):
        super().__init__(name, distance, orbit_time)

    def details(self):
        print(self.name, "is", self.distance, "AU from the sun.")
        print(self.name, "takes", self.orbit, "years to orbit the sun.")

    def spin(self):
        print(self.name, "spins like crazy.")


Halley_Comet = Comets("Halley's Comet",35.1, 76)
Hale_Bopp = Comets("Hale-Bopp",370, 2534)

print("Earth Results:")
Earth.details()
Earth.spin()
Earth.colonization()

print("Mars Results:")
Mars.details()
Mars.spin()
Mars.colonization()

print("Halley's Comet Results:")
Halley_Comet.details()
Halley_Comet.spin()
Halley_Comet.colonization()

print("Hale-Bopp Comet Results:")
Hale_Bopp.details()
Hale_Bopp.spin()
Hale_Bopp.colonization()

#These are my results from running the program, and I am very happy with how it turned out. I did run into an issue where
# my default value for Earth was being read as a tuple due to my use of commas, but that was the only major bug I ran into.
# This lab really showed me how useful classes and the architecture of parent and child classes can really be. There were
# a few different changes I wanted to make as far as what I wanted to print, and I really only need to edit one or two lines
# of code to have the whole thing update, which was super nice.

'''
Earth Results:
Earth is 1 AU from the sun.
Earth takes 365 days to orbit the sun.
Earth spins slightly elliptical.
Earth has a colonization score of 6000000000.0
Mars Results:
Mars is 1.5 AU from the sun.
Mars takes 687 days to orbit the sun.
Mars spins slightly elliptical.
Mars has a colonization score of 4000000000.0
Halley's Comet Results:
Halley's Comet is 35.1 AU from the sun.
Halley's Comet takes 76 years to orbit the sun.
Halley's Comet spins like crazy.
Halley's Comet has a colonization score of 170940170.94
Hale-Bopp Comet Results:
Hale-Bopp is 370 AU from the sun.
Hale-Bopp takes 2534 years to orbit the sun.
Hale-Bopp spins like crazy.
Hale-Bopp has a colonization score of 16216216.22
'''