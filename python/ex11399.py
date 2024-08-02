import sys

N = int(sys.stdin.readline())
P = sorted(map(int, sys.stdin.readline().split()))

sum = 0
for i in range(N):
    sum += P[i] * (N - i)

print(sum)