import sys

N, M = map(int, sys.stdin.readline().split())

A = [[0 for col in range(M)] for row in range(N)]
B = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    A[i] = list(sys.stdin.readline())
for i in range(N):
    B[i] = list(sys.stdin.readline())

for i in range(N):
    for j in range(M):
        A[i][j] = int(A[i][j])       
for i in range(N):
    for j in range(M):
        B[i][j] = int(B[i][j])

cnt = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            cnt += 1
            for x in range(3):
                for y in range(3):
                    if A[i + x][j + y] == 0:
                        A[i + x][j + y] = 1
                    else:
                        A[i + x][j + y] = 0

if A == B:
    print(cnt)
else:
    print(-1)