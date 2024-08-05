import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr_up = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and arr_up[j] + 1 > arr_up[i]:
            arr_up[i] = arr_up[j] + 1

arr_down = [1] * N 
for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j] and arr_down[j] + 1 > arr_down[i]:
            arr_down[i] = arr_down[j] + 1
            
arr = [0] * N
for i in range(N):
    arr[i] = arr_up[i] + arr_down[i] - 1

print(max(arr))