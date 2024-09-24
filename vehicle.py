class vehicle:
    def __init__(self,wheels,fuelType):
        self.wheels = wheels
        self.fuelType = fuelType
        
    def start(self):
        self.running=True
        print("key In,key spin, put gear and push vehicle")
        
class Bike(vehicle):
    def kickstart(self):
        self.running=True
        print("key In,and kick")
        
    def pushStart(self):
        self.start()
        
b1=Bike(2,"petrol")
b2=Bike(2,"deisel")

b1.kickstart()
b2.pushStart()
        