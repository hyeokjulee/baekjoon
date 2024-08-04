import sys

d = [0, 1, 2, 4]
nh = []
T = int(sys.stdin.readline())
result = [0] * T

for i in range(T):
    n = int(sys.stdin.readline())
    nh.append([n, i])

nh.sort()

for i in range(1, 4):
    while nh and nh[0][0] == i:
        result[nh.pop(0)[1]] = d[i]

for i in range(4, 1000001):
    d[0] = d[1]
    d[1] = d[2]
    d[2] = d[3]
    d[3] = (d[0] + d[1] + d[2]) % 1000000009
    while nh and nh[0][0] == i:
        result[nh.pop(0)[1]] = d[3]

for i in range(T):
    print(result[i])