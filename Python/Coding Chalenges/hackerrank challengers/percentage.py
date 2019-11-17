N = int(input())
dictOfStudentsRaw = {}

for i in range(0, N):
    studentInput = input()
    studentName = studentInput.split(" ", 1)[0]
    studentScore = studentInput.split(" ", 1)[1]
    dictOfStudentsRaw[studentName] = studentScore
outputStudent = input()

for key in dictOfStudentsRaw:
    if str(key) == outputStudent:
        scores = dictOfStudentsRaw.get(key)
        scoreslist = scores.split()
        average = 0
        for i in range(0, len(scoreslist)):
            average += float(scoreslist[i])
        average = average / len(scoreslist)
        print("{0:.2f}".format(average))
