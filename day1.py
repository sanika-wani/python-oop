
class Car:
    make=None
    color =None
    model=None
    
    def __init__(self,make,model,color): #self reference . reference to itself
        self.__make=make
        self.model=model
        self.color=color
        
    def __str__(self):
        return f"{self.color}-{self.__make}-{self.model}"
    
    # def __repr__(self):
    #     return f"{self.color}-{self.model}-{self.__make}"
    
    def getmake(self):
        return self.__make
    
    def SetMake(self,make):
        self.__make = make
        print('Car updated !')
    
car1= Car('Hyundai','swift','white')
car2 = Car('Maruti','levo','black')
# print(car1.color)
# print(car2.model)
# print(car1)
# print(car1.getmake())
# print(car1.SetMake('kia'))

print(car1)
 

# class beta:
#     pass
# b1= beta()
# print(b1)        
# b1.name ="first object"
# print(b1.name)
# print(car1==car2)
# del car1

# del car2 
