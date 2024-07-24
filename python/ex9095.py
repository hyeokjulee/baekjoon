import sys

d = [1, 2, 4]
for i in range(3, 10):
    d.append(d[i - 1] + d[i - 2] + d[i - 3])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n - 1])