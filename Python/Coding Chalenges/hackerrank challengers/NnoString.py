def printNumbersTo(n):
    out = ""
    for i in range(1, n+1):
        out = out + str(i)
    print(out)


rawinput = input("enter number to print to: ")
printNumbersTo(int(rawinput))