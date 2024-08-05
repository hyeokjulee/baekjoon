import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = [0] * 20
for a in A:
    for i in range(20):
        if a & 2 ** i:
            arr[i] += 1 

print(max(arr))