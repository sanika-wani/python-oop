# friendList = {
#     "jane": "offline",
#     "harry": "online",
#     "marie" : "online",
#     "ron": "offline",
#     "fred" : "online",
# }
# a=0
# b=0
# #loop through a dictionary
# for key, value in friendList.items():
#     if value == "online":
#         a+=1
#     else:
#         b+=1
        
# print("online: ", a, " "+" offline: ",b)


        
# print("online: ", a, " "+" offline: ",b)

# messages = {
#     "jane": [],
#     "harry": [],
#     "marie" : [],
#     "ron": [],
#     "fred" : [],
# }
# usr= friendList.keys()
# msg="hello"

# def sendMessage(usr,msg):
#     for (key1, value1), (key2, value2) in zip(friendList.items(), messages.items()):
#         if value1 == "online":
#             messages[key2].append(msg)
#     return messages

# sendMessage(usr,msg)
# print(messages)

#chicken3,goat9,cow2,snake11 
#farm1: xlegs, farm2:x*2 legs
# Animals ={
#     "chicken":2,
#     "goat":4,
#     "cow":4,
#     "snake":0
# }

class animal:
    count = 0
    legs = 2
    id_counter = 0  
    def __init__(self):
        self.id = animal.id_counter  
        animal.id_counter += 1 
    def legst(self):
        return self.count * self.legs

class animal:
    count=0
    legs=2
    def legst(self):
        return self.count*self.legs

class chic(animal):
    def _init_(self,count):
        self.count=count
        self.legs=2
        
class goat(animal):
    def _init_(self,count):
        self.count=count
        self.legs=4
        
class cow(animal):
    def _init_(self,count):
        self.count=count
        self.legs=4
        
class snake(animal):
    def _init_(self,count):
        self.count=count
        self.legs=0
        
class farm:
    def _init_(self,ch,go,co,sk):
        self.chic = chic(ch)
        self.goat = goat(go)
        self.cow = cow(co)
        self.snake = snake(sk)

def _str_(self)->str:
    return f"{self.chic.legst()+self.goat.legst()+self.cow.legst()+self.snake.legst()}"

def _repr_(self)->str:
    return f"{self.chic.legst()+self.goat.legst()+self.cow.legst()+self.snake.legst()}"

