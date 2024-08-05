import sys, bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = []
length_of_arr = 0
for i in range(N):
    idx = bisect.bisect_left(arr, A[i])
    if idx == length_of_arr:
        arr.append(A[i])
        length_of_arr += 1
    else:
        arr[idx] = A[i]

print(length_of_arr)