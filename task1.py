class shape:
    color =None
    type = None
    
    def __init__(self,color,type):
        self.color = color
        self.type = type
        
    def __str__(self):
        return f"{self.color}-{self.type}"

#child class
class circle(shape):
    radius=None
    def __init__(self,color,radius):
        super().__init__(color,"circle")
        self.radius= radius
        
    def __str__(self):
        return f"{super().__str__()}, circle_radius: {self.radius}"
Circle= circle("Blue",5.0)
print(Circle)

