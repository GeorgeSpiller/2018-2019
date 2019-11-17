def ifthenelse(data):
    if (data % 2) != 0:
        print("Weird")
    elif((data % 2) == 0) and (2 <= data <= 5):
        print("Not Weird")
    elif((data % 2) == 0) and (6 <= data <= 20):
        print("Weird")
    elif(data > 20):
        print("Not Weird")




if __name__ == '__main__':
    inputdata = int(input())
    ifthenelse(inputdata)