import sys

d = [0, 1, 2, 2, 3, 3, 6]
for i in range(7, 100001):
    d.append((d[i - 2] + d[i - 4] + d[i - 6]) % 1000000009)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])