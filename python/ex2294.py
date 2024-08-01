import sys

n, k = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

d = [0] * (k + 1)
for i in range(1, k + 1):
    tmp = []
    for j in a:
        if i - j >= 0 and d[i - j] >= 0:
            tmp.append(d[i - j])
    if tmp:
        d[i] = min(tmp) + 1
    else:
        d[i] = -1

print(d[k])