def merge_the_tools(string, k):
    tmpList = []
    tDict = []
    newSeg = ""
    outputlist = []

    for i in range(0, len(string), k):
        tmpList.append(string[i:i+k])


    for tSegment in tmpList:
        tDict = []
        for x in range(0, len(tSegment)):
            if(tSegment[x] not in tDict):
                tDict.extend(tSegment[x])
                newSeg += tSegment[x]

        outputlist.append(newSeg)
        newSeg = ""

    for entity in outputlist:
        outp = entity
        outp = outp.replace("'","")
        outp = outp.replace(",","")
        print(outp)
 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
