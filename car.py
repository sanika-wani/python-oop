class Car:
    def __init__(self,make,model,color): #self reference . reference to itself
        self.__make=make
        self.model=model
        self.color=color
    def SetMake(self,make):
        self.__make = make
        print('Car updated !')
    def __str__(self):
        return f"{self.color}-{self.__make}-{self.model}"
    
    def __repr__(self):
        return f"{self.color}-{self.__make}-{self.model}"
    
    def getmake(self):
        return self.__make

cl=[
    Car('Hyundai','hp','white'),
    Car('Hyundai','levo','blue')
    ,Car('Hyundai','swift','green'),
    Car('Hyundai','swift','red')
]


def searchByColor(color):
    result= "color not found"
    for c in cl:
        if c.color==color:
            result =f"color found on {c}"
            break
    print(result)
searchByColor('white')