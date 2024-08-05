import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = [1] * N

for i in range(1, len(A)):
    for j in range(i):
        if A[i] > A[j] and arr[j] + 1 > arr[i]:
            arr[i] = arr[j] + 1

print(max(arr))