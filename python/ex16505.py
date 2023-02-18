import sys

def listMtoN(x): # 재귀 함수
    if x == 0:
        return [['*']] # listMtoN(0) = [['*']]

    listM = listMtoN(x - 1) # 재귀 호출

    listN = [[] for i in range(2 ** x)] # 리스트 생성

    for i in range(2 ** x , 0, -1):
        for j in range(i):
            listN[2 ** x - i].append(' ') # 리스트의 값들은 일단 모두 공백으로 초기화하며 전체적인 모양의 틀을 잡는다.

    for i in range(2 ** (x - 1), 0, -1):
        for j in range(i):
            listN[2 ** (x - 1) - i][j] = listM[2 ** (x - 1) - i][j] # 좌측 상단 부분 채워줌
            listN[2 ** (x - 1) - i][j + 2 ** (x - 1)] = listM[2 ** (x - 1) - i][j] # 우측 상단 부분 채워줌
            listN[2 ** x - i][j] = listM[2 ** (x - 1) - i][j] # 좌측 하단 부분 채워줌

    return listN

N = int(sys.stdin.readline()) # 정수 입력

outList = listMtoN(N) # 재귀 함수 실행

for i in range(2 ** N, 0, -1):
    for j in range(i):
        print(outList[2 ** N - i][j], end='')
    print()