def swap_case(s):
    s = str(s)
    outputstr = ""
    for i in range(0, len(s)):
        if (s[i].islower()):
            outputstr += s[i].upper()
        elif (s[i].isupper()):
            outputstr += s[i].lower()
        else:
            outputstr += s[i]
    return outputstr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)