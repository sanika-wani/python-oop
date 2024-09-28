friendList = {
    "jane": "offline",
    "harry": "online",
    "marie" : "online",
    "ron": "offline",
    "fred" : "online",
}
a=0
b=0
#loop through a dictionary
for key, value in friendList.items():
    if value == "online":
        a+=1
    else:
        b+=1
        
print("online: ", a, " "+" offline: ",b)
    