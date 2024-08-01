import sys

n, k = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

d = [0] * (k + 1)
d[0] = 1 
for i in a:
    for j in range(i, k + 1):
        d[j] += d[j - i]

print(d[k])