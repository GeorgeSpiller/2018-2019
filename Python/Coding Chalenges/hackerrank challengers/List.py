if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = j = k = 0
    ar = []
    for i in range(i+1):
        for j in range(j+1):
            for k in range(k+1):
                if ((i + j + k) != n):
                    ar.append("[{}, {}, {}]".format(i, j, k))
    #print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
    for things in range(0, len(ar)):
        print(ar[things])





