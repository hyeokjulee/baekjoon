import sys, copy

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = copy.deepcopy(A)

for i in range(1, len(A)):
    for j in range(i):
        if A[i] > A[j] and arr[j] + A[i] > arr[i]:
            arr[i] = arr[j] + A[i]

print(max(arr))