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
    
class sparrow(bird):
    def sound(self):
        print("chirp-chirp")
        
    def __str__(self):
        return f"This is a sparrow | {super().__str__()}"
    
class crow(bird):
    def sound(self):
        print("crow-crow")
        
    def __str__(self):
        return f"This is a bird | {super().__str__()}"    
    
d=[
    duck(False,"yellow","medium"),
    duck(False,"white","small"),
    sparrow(True,"black","small"),
    crow(True,"black","large"),]

def countSpecies():
    a=0
    b=0
    c=0
    for i in d:
        if isinstance(i,duck)==True:
            a=a+1
        if isinstance(i,sparrow)==True:
            b=b+1
        if isinstance(i,crow)==True:
            c=c+1
    result=f"duck:{a}, sparrow:{b}, crow:{c}"
    print(result)
countSpecies()

