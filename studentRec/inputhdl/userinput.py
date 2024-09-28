
def showError(title,message):
    print(f"""
    #######################
    ##|> {title}
    ##|> {message}
    #######################
    """)


def getString(msg):
    return input(msg+": ")

def getInt(msg):
    v = input(msg+": ")
    try:
        v = int(v)
    except ValueError:
        showError(
            'Invalid Input!',
            'Please Enter Numbers only (no spaces)'
            )
        return getInt(msg)
    else: 
        return v

fnMap = {
    "int":getInt,
    "str":getString
}

def printMenu(itr):
    print("▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥\n▥▥")
    for i,v in enumerate(itr):
        print(f"▥▥\tEnter {i} for '{v}'")
    print("▥▥\n▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥")


def collectData(dKeys,dTypes,prompts):
    xDictn = dict.fromkeys(dKeys)
    for ind,key in enumerate(dKeys):
        xDictn[key] = fnMap[ dTypes[ind] ](prompts[ind])
    return xDictn