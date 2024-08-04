import sys

d = [[], [1, 0], [1, 1], [2, 2]]
for i in range(4, 100001):
    d.append([(d[i - 1][1] + d[i - 2][1] + d[i - 3][1]) % 1000000009, (d[i - 1][0] + d[i - 2][0] + d[i - 3][0]) % 1000000009])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n][0], d[n][1])