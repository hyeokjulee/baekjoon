import sys

d = [0, 1, 2, 3]
for i in range(4, 10001):
    if i % 3 == 0:
        d.append(d[i - 1] + d[i - 2] - d[i - 3] + 1)
    else:
        d.append(d[i - 1] + d[i - 2] - d[i - 3])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])