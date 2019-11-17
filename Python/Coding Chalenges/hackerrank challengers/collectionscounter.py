from collections import Counter
#We dont even end up pusing this imported function
# but it looks usefull so theres some commented code
# at the bottom on how to use it

#The first line contains X, the number of shoes.
shoeTotal = input("Total number of shoes:")
#The second line contains the space separated list of all the shoe sizes in the shop.
shoeSizes = input("Shoe Sizes:").split()
#The third line contains N, the number of customers.
NumberOfCustomers = int(input("Number of customers:"))
#The next N lines contain the space separated values of the  desired by the customer and , the price of the shoe.
CustomerList = []
for i in range(0,NumberOfCustomers):
    CustomerList.append(input().split())

total = 0
#Start the sorting
for i in range(0, len(CustomerList)):
    if CustomerList[i][0] in shoeSizes:
        total += int(CustomerList[i][1])
        shoeSizes.remove(CustomerList[i][0])

print(total)
"""
myList = [7,7,7,7,9,9,9,2]
#   format is ({value:number of occurances, ...)}
#    sorted from highest occurance to lowest occurance
#print(Counter(myList)) 

#    you can isolate only the unique values
#print(Counter(myList).keys())
#    and only print the number of occurances
#print(Counter(myList).values())

#remove value from counter:
#myList.remove(9) #argument is the value to remove
"""
