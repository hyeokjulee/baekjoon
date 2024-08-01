import sys

N, K = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(int(sys.stdin.readline()))

cnt = 0
idx = N - 1
while K != 0:
    cnt += K // A[idx]
    K = K % A[idx]
    idx -= 1

print(cnt)
