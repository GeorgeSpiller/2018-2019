pin =  str(input("enter digits: "))

for a in range(0,4):
    for b in range(0,4):
        for c in range(0,4):
            for d in range(0,4):
                if a==b or a==c or a==d or b==c or b==d or c==d:
                    continue
                print(pin[a]+pin[b]+pin[c]+pin[d])
                


