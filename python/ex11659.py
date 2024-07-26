import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

sum = [0]
for i in range(N):
    sum.append(num[i] + sum[i])

for _ in range(M):
    start, stop = map(int, sys.stdin.readline().split())
    print(sum[stop] - sum[start - 1])