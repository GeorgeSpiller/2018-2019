inp = input().split()
k = int(inp[0])
m = int(inp[1])
NList = []
outp = 0
for i in range(0, k):
    inp = input()
    NList.append(inp.split()[1:])
#----------------------------------------
# squ all values in all the sublists
for indx, val in enumerate(NList):
    NList[indx] = [int(x)**2 for x in val]
print(NList)

parsList = [] # the list we will use to parse into func()
def loop(mainList, CurrentSublist):
    global parsList
    def func(x):
        global outp
        if (sum(x)%m) > outp:
            #print("Current Parse List highest: {}".format(x))
            outp = sum(x)%m
    for val in CurrentSublist:
        parsList.append(val)
        # go to the next itteratin only if all the next lists
        # have been looped over
        #print(" MainList : {}\n In Sublist: {}\n On Val: {}\n Parse: {}\n------".format(mainList, CurrentSublist, val, parsList))
        try:  # try t go to the next sublist
            # we are here if we still have sublists to go
            loop(mainList, mainList[(mainList.index(CurrentSublist)+1)])
            parsList.pop()
        except IndexError: # if we are at the last sub list
            func(parsList)
            # we are here if we have reached the end of the final sublist
            parsList.pop()
loop(NList, NList[0])
# parse in a list of the values you want to use in the func
print(outp)







