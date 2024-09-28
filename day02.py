# import os
# def scanFolder(rootPath):
#     for dirpath, dirNames, filenames in os.walk(rootPath):
#         print(f"\t->items under {dirpath}: ")
#         for dirName in dirNames:
#             print(dirName)
#             scanFolder(dirName)
#         print(f"Files: ")
#         for fileName in filenames:
#             print(fileName)
# scanFolder("c:\\xampp\\htdocs")
# type 26520 and answer in words

#enumerate

name = input("enter name:")
print(f"Your name is {name}")
try:
    age = int(input("Enter your age: "))
    if (age>17):
        print("you can drive")
    else:
        print("you are too young to drive")
except ValueError:
    print("wrong input, please try again")