from abc import ABC,abstractmethod


class bird(ABC):
    def __init__(self,canFly,color,size):
        self.__canFly=canFly
        self.__color=color
        self.__size=size
        
    def __str__(self):
        return f"Can Fly:{self.__canFly} | color: {self.__color}"
        
    #descriptor for interpretor to understand type of declaration
    @abstractmethod
    def sound(self):
        pass
    
class duck(bird):
    def sound(self):
        print("Quack-Quack")
        
    def __str__(self):
        return f"This is a duck | {super().__str__()}"
    
d=duck(False,"yellow","medium")
d.sound()
print(d)