from itertools import permutations
def printPerms(imp):
    outp = ""
    #sanitise smelly input
    St = list(str(imp).split(" ")[0])
    k = int(str(imp).split(" ")[1])
    #print('S= {} and K= {}'.format(St, k))
    outputlist = list(permutations(St, k))
    outputlist.sort()
    for i in range(0, len(outputlist)):
        sanOut = str(outputlist[i])
        sanOut = sanOut.replace("'", "")
        sanOut =  sanOut.replace(")", "")
        sanOut =  sanOut.replace("(", "")
        sanOut =   sanOut.replace(",", "")
        sanOut =   sanOut.replace(" ", "")
        outp = outp + '\n' + sanOut
    print(outp.strip())


rawinput = input(">>")
printPerms(rawinput)