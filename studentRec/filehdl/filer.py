import os
def saveData(fn,data):
    success = False
    try:
            theFile = open(fn,'w')
            theFile.write(data)
            print(f"File {fn} Saved")
            success==True
    except:
        print(f"error saving file: {fn}")
    finally:
        theFile.close()
    return success

def loadData(fn):
     data =''
     try:
            theFile = open(fn,'r')
            data = theFile.read()            
     except:
        print(f"Error Reading file {fn}" )
     finally:
        theFile.close()
     return data

def delData(fn):
       success = False
       try:
            os.remove(fn)
            success=True
       except FileNotFoundError:
            print("The file does not exist")
       else:
            print("File deleted successfully!")
       return success