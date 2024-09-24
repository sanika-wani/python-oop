class students:
    id=None
    name=None
    age=None
    score=None
    gender=None
    
    def __init__(self,id,name,age,score,gender):
        self.id=id
        self.name=name
        self.age=age
        self.score=score
        self.gender=gender
        
s=[students(1,'sanika',19,91,'F'),
   students(2,'raghav',29,61,'M'),
   students(3,'karishma',49,99,'F'),
   students(4,'soham',16,99,'M'),
   students(5,'sirri',13,100,'F'),
   students(6,'sara',11,92,'F'),
   students(7,'sam',10,94,'M'),
   students(8,'savi',20,99,'F')
   ]

userInput= input("Search User: ")

def searchUser(name):
    result="User not found"
    for i in s:
        if i.name==name:
            result=f"User found with id {i.id} and name {i.name}"
            break
    print(result)   
searchUser(userInput)

def maxScore():
    max_score = 0
    max_students = []
    for i in s:
        if i.score > max_score:
            max_score = i.score
            max_students = [i]
        elif i.score == max_score:
            max_students.append(i)
    if len(max_students) == 1:
        print(f"Max score is {max_score} by {max_students[0].name} with id {max_students[0].id}")
    else:
        print(f"Max score is {max_score} by:")
        for student in max_students:
            print(f"  - {student.name} with id {student.id}")
maxScore()

        