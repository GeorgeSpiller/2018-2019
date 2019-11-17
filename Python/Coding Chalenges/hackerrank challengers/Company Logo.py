from collections import Counter
"""

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

"""

s = input()
letters = []
outp = []
countnum = []
for i in range(0, len(s)):
    letters.append(s[i])

letters = Counter(letters)
for characters, count in letters.most_common(3):
    outp.append(characters)
    countnum.append(count)

if (len(Counter(countnum).keys()) < 3):
    #sort alphabetically
else:
    #sort decending
    outputlist = outp.sorted(outputlist reverse = True)
    for i range(0, len(outputlist)):
        print("{} {}\n".format(outputlist[i], ))
         



#   format is ({value:number of occurances, ...)}
#    sorted from highest occurance to lowest occurance
#print(Counter(myList)) 

#    you can isolate only the unique values
#print(Counter(myList).keys())
#    and only print the number of occurances
#print(Counter(myList).values())

#remove value from counter:
#myList.remove(9) #argument is the value to remove