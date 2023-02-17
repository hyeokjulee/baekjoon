import sys

def listMtoN(x): # 재귀함수
    if x == 0:
        return [['*']]

    listM = listMtoN(x - 1).copy()

    listN = [[] for i in range(2 ** x)]

    for i in range(2 ** x - 1, -1, -1):
        for j in range(i + 1):
            listN[2 ** x - 1 - i].append(' ')

    for i in range(2 ** (x - 1) - 1, -1, -1):
        for j in range(i + 1):
            listN[2 ** (x - 1) - 1 - i][j] = listM[2 ** (x - 1) - 1 - i][j]
            listN[2 ** x - 1 - i][j] = listM[2 ** (x - 1) - 1 - i][j]
            listN[2 ** (x - 1) - 1 - i][j + 2 ** (x - 1)] = listM[2 ** (x - 1) - 1 - i][j]

    return listN

N = int(sys.stdin.readline())

outList = listMtoN(N)

for i in range(2 ** N - 1, -1, -1):
    for j in range(i + 1):
        print(outList[2 ** N - i][j], end='')
    print()