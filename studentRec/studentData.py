from inputhdl import userinput
from filehdl import filer
#Defined the function to accept inputs 
#and store them in a Dictionary and later append to a list 
students = []
running = True
dKeys = ('name','age','score')
#for loop for printing formatted table
def printList(stdList):
    for stdt in stdList:
        print(f"Name: {stdt["name"]}, Score: {stdt["score"]}")

def exitCode():
    global running
    running=False
    print('BYE!!!')

def addEntry():
    try:
        student = userinput.collectData(dKeys,('str','int','int'),["Enter Name","Enter Age","Enter Score"])
        if student["age"] > 30:
            raise Exception("Invalid Age!")
        students.append(student)
        print("\n\n***Entry Added!!!***\n\n\n")
    except:
        print("Invalid Age, Please try again")

def saveData():
    printList(students) if filer.saveData("students.txt",str(students)) else None

def loadData():
    global students
    students = eval( filer.loadData("students.txt"))
    printList(students)

def delData():
    'Data deleted!' if filer.delData("students.txt") else 'No Data was deleted!'

def searchData():
    name = userinput.getString("Enter name of Student(s): ")
    printList(list ( filter ( 
            lambda listItem: name.lower() in listItem["name"].lower() ==name,
            students 
        ) ) )

menuMap = { 0:exitCode,1:addEntry,2:saveData,3:loadData,4:delData,5:searchData}

while(running):
    userinput.printMenu(['Exit','Add Entry','Save Data', 'Load Data', 'Delete All Dat','Search'])
    inp = userinput.getInt("Enter your Option from above: ")
    menuMap[inp]() if inp<6 and inp>-1 else print("\nPlease Enter a valid Option!\n")