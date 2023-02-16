import sys

def listMtoN(x): # 재귀함수
    if x == 0:
        return ['*']

    listM = listMtoN(x - 1).copy()

    for i in range(2 ** x, 0, -1):
        listN = [[' ' for col in range(i)] for row in range(2 ** x)]

    for i in range(2 ** (x - 1), 0, -1):
        for j in range(i):
            listN[i][j] = listM[i][j]
            listN[i + 2 ** (x - 1)][j] = listM[i][j]
            listN[i][j + 2 ** (x - 1)] = listM[i][j]

    return listN

N = int(sys.stdin.readline().rstrip('\n'))

outList = listMtoN(N)

for i in range(2 ** N, 0, -1):
    for j in i:
        print(outList[i][j], end='')
    print()