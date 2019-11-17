def print_formatted(number):
    data = int(number)
    for i in range(1, int(data)+1):
        width = " "*len("{0:b}".format(n))
        printout = ""
        printout = printout + str(int(i)) + width
        printout = printout + str(oct(i)[2:]) + width
        printout = printout + str(hex(i)[2:].upper()) + width
        printout = printout + str(bin(i)[2:])
        #print("{} {} {} {}".format(int(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]))
        print(printout)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
