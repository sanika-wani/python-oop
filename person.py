class person:
    name =None
    age = None
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class student(person):          #name of parent class in parenthesis
    type="Student person"

p1= person("Sanika",19)
p2=student("karishma",19)
print(p1)
#inheritence code remaining
