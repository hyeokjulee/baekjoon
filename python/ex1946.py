import sys

for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline()) # 지원자의 숫자
    A = [] # 지원자의 서류심사 성적, 면접 성적의 순위
    for j in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
    A.sort()

    min = A[0][1]
    for j in range(1, N):
        if A[j][1] > min:
            N -=1
        else:
            min = A[j][1]
    print(N)