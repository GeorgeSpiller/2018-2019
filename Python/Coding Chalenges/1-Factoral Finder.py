def Factoral_Example(itterations):#n - (x+1)
    for x in range(1,itterations):
        print(n-(x+x))

def Factoral_Normal(itterations):
    for x in range(1,itterations):
        print(n*(x*x))


n=1
x=0
trys = int(input("How manny itteraions?: "))
Ftype = input("Normal (n*(x*x)) or Example (n(x*x))?: ")
if Ftype[0].lower() == "n":
    Factoral_Normal(trys)
else:
    Factoral_Example(trys)
