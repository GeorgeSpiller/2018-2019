data = input("Enter Dimentions: ").split()
n = int(data[0])
m = int(data[1])
fillerLines = int(n/2)
patternFill = 3
for i in range(1, fillerLines+1):
    lineOutput = ""  
    dashSeg = int((m - patternFill) / 2)
    lineOutput = lineOutput + ("-" * dashSeg )
    lineOutput = lineOutput + (".|." * (int(patternFill/3)))
    lineOutput = lineOutput + ("-" * dashSeg )
    patternFill += 6 
    print(lineOutput)


print(("-" * int(((m-7)/2))) + "WELCOME" + ("-" * int(((m-7)/2))))
patternFill -= 6 
for i in range(1, fillerLines+1):
    lineOutput = ""  
    dashSeg = int((m - patternFill) / 2)
    lineOutput = lineOutput + ("-" * dashSeg )
    lineOutput = lineOutput + (".|." * (int(patternFill/3)))
    lineOutput = lineOutput + ("-" * dashSeg )
    patternFill -= 6 
    print(lineOutput)