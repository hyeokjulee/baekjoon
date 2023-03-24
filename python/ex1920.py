import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    target = B[i]
    start = 0
    end = N - 1
    while True:
        mid = (start + end ) // 2
        if start > end:
            print(0)
            break
        elif A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        else:
            print(1)
            break