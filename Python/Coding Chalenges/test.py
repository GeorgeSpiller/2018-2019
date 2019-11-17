def isLeapYear(year):
    '''
    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.
    '''
    leap = False
    year = int(year)
    if (year % 4 == 0):
        if (year % 100 == 0) and (year % 400 == 0):
            leap = True
        if (year % 100 != 0):
            leap = True

    print(leap)
while True:
    testint = input("enter year to check: ")
    isLeapYear(testint)