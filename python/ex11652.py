import sys

inputDict = {}
for _ in range(int(sys.stdin.readline())): # 개수 입력
    inputNum = int(sys.stdin.readline()) # 정수 입력
    if inputNum in inputDict:
        inputDict[inputNum] += 1 # key 값이 있으면 기존 value 값에 + 1
    else:
        inputDict[inputNum] = 1 # key 값이 없으면 value 값 = 1

inputDict = dict(sorted(inputDict.items())) # key 값 기준 오름차순으로 정렬

print(sorted(inputDict.items(), key=lambda x: x[1], reverse=True)[0][0]) # value 값 기준 내림차순으로 정렬