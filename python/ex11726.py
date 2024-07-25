import sys

n = int(sys.stdin.readline())

d = [1, 2]
for i in range(2, n):
    d.append(d[i - 1] + d[i - 2])

print(d[n - 1] % 10007)