#billing system for a tea stall

def TeaStall():

    print("---------tea stall--------")
    print("1.tea-------------------10")
    print("--------------------------")
    print("2.coffee----------------40")
    print("--------------------------")
    pt,pc=10,40
    print(" Number of tea and coffe you wish to have?")
    t,c=map(int,input().split())
    print(f"Your order is tea:{t}  coffee:{c}")
    if t>0 or c>0:
        print("------------Bill--------------")
    if t>0:
        print(f"Tea: {t*pt}")
    if c>0:
        print(f"Coffee: {c*pc}")
    

while True:
    ch = input("want to order: ..? (y/n)")
    if ch == 'y' or ch == 'Y':
        TeaStall()
        pass
    elif ch == 'n' or ch == 'N':
        print("Thanks visit again")
    else :
        print("enter vaid input")

