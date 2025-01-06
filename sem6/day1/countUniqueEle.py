data=[11,22,11,22,44,55,66,11]
for item in sorted(set(data)):
    print(item,"--->", data.count(item))


#2nd largest element
print(sorted(data)[-2])
#4th smalllest element
print(sorted(data)[3])