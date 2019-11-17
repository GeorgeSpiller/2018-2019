if __name__ == '__main__':
    s = input()
    alnum=alpha=didgit=lower=upper = False
    for i in range(0, len(s)):
        case = s[i]
        if (case.isalnum()):
            alnum = True
        if (case.isalpha()):
            alpha = True
        if (case.isdigit()):
            didgit = True
            '''
        print("Value: {}".format(chr(int(case))))
        try:
            print("Value: {}".format((chr(int(case)).isdidgit())))
            if (chr(int(case)).isdidgit()):
                didgit = True
                
        except:
            pass
            '''
        if (case.islower()):
            lower = True
        if (case.isupper()):
            upper = True

    print("{}\n{}\n{}\n{}\n{}".format(alnum,alpha,didgit,lower,upper))
            

'''
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())
    '''