from collections import Counter
def raw_input():
    return input()

student = []
classlist = []
for _ in range(int(raw_input())):
    student.append(raw_input())
    student.append(float(raw_input()))
    classlist.append(student)
    student = []

def GetStudentName(index):
    name = index[0]
    return name
def GetStudentScore(index):
    score = index[1]
    return score
def Get2ndLowestScore():
    scorelist = []
    for i in range(0,len(classlist)):
        scorelist.append(classlist[i][1])
    score = sorted(list(Counter(scorelist).keys()))[1]
    return score


#print(Sort(classlist))
ClassListNames = sorted(classlist, key=GetStudentName)
ClassListScores = sorted(classlist, key=GetStudentScore)
#print('normal:{}\nnames:{}\nScores:{}'.format(classlist,ClassListNames, ClassListScores))
#Print names with 2nd lowest scores 

SecondLowestScore = Get2ndLowestScore()
output = []
for i in range(0, len(ClassListScores)):
    if ClassListScores[i][1] == SecondLowestScore:
        output.append(ClassListScores[i][0])

output.sort()
for x in range(0, len(output)):
    print(output[x])
'''
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
'''