def raw_input():
    return (input())

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    arr = list(arr)

    arr.sort()
    arr = list(dict.fromkeys(arr))
    print(arr[len(arr) - 2])

    
