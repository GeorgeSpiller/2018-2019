from collections import Counter
n = input()
arr = input().split()
keyList = list(Counter(arr).keys())
keyList = [ int(x) for x in keyList ]
newList = sorted(keyList, reverse=True)

print(newList[1])