from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod           # =====
    def make_sound(self):     # >>>>=> [ This is abstraction_class]
        pass                  #======   

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class cat(Animal):
    def make_sound(self):
        print("Mewo!")

class Cow(Animal):
    def make_sound(self):
        print("hama!")

class Dog(Animal):
    def make_sound(self):
        print("Bohw Bhow!")

class Bear(Animal):
    def make_sound(self):
        print("Kduru kudru!")

class Bofalo(Animal):
    def make_sound(self):
        print("wowee!")

class Pig(Animal):
    def make_sound(self):
        print("ghreerrr!")

lion = Lion()

lion.make_sound()

cow = Cow()  
cow.make_sound()

pig = Pig()
pig.make_sound()

