
def cubes(data):
    #sanatize the smelly input
    NoOfCases = data[0]
    data.split('\n')
    print(data)



if __name__ == '__main__':
    inputdataamount = raw_input()[0]
    data = ""
    for i in range(0,inputdataamount*2):
        data += input()
    cubes(data)
    
