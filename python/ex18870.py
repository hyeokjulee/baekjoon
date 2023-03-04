import sys

N = int(sys.stdin.readline())

xList, xxList = list(map(int, sys.stdin.readline().split())), [[0 for col in range(3)] for row in range(N)]

for i in range(N):
    xxList[i][0], xxList[i][1] = xList[i], i

xxList.sort(key=lambda a:a[0])

xx = 0
for i in range(N - 1):
    xxList[i][2] = xx
    if xxList[i][0] < xxList[i + 1][0]:
        xx += 1
xxList[N - 1][2] = xx

xxList.sort(key=lambda a:a[1])

for x in xxList:
    print(x[2], end=' ')