import sys, bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = []
d = []
length_of_arr = 0
for i in range(N):
    idx = bisect.bisect_left(arr, A[i])
    if idx == length_of_arr:
        arr.append(A[i])
        length_of_arr += 1
        d.append([idx, A[i]])
    elif arr[idx] != A[i]:
        arr[idx] = A[i]
        d.append([idx, A[i]])

result = []
last_idx = max(d)[0]
for i in range(len(d) - 1, -1, -1):
    if d[i][0] == last_idx:
        result.append(d[i])
        last_idx -= 1

print(length_of_arr)
for i in range(len(result) - 1, -1, -1):
    print(result[i][1], end=' ')