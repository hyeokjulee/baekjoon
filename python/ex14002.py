import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr_of_length = [1] * N
arr_of_numberList = [[A[i]] for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and arr_of_length[j] + 1 > arr_of_length[i]:
            arr_of_length[i] = arr_of_length[j] + 1
            arr_of_numberList[i] = arr_of_numberList[j] + [A[i]]

idx = arr_of_length.index(max(arr_of_length))

print(arr_of_length[idx])
print(' '.join(map(str, arr_of_numberList[idx])))