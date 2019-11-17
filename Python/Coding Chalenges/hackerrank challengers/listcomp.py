n = int(input())
outplist = []
args= []
inputs = []
for i in range(0, n):
    inputs.append(input())
for i in range(0, len(inputs)):
    if inputs[i].split()[0] == "insert":
        args = inputs[i].split()[1:]
        outplist.insert(int(args[0]), int(args[1]))
    elif inputs[i].split()[0] == "remove":
        args = inputs[i].split()[1]
        if int(args) in outplist:
            outplist.remove(int(args))
    elif inputs[i].split()[0] == "append":
        args = inputs[i].split()[1]
        outplist.append(int(args))

    elif inputs[i].split()[0] == "sort":
        outplist.sort()

    elif inputs[i].split()[0] == "pop":
        outplist.pop()

    elif inputs[i].split()[0] == "reverse":
        outplist.reverse()
    elif inputs[i].split()[0] == "print":
        print(outplist)
    else:
        pass
