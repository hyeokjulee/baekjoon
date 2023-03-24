import sys

X = int(sys.stdin.readline())

d = [0] * (X + 1)

d[2], d[3], d[4], d[5] = 1, 1, 2, 1

for i in range(6, X + 1):
    li = [d[i - 1]]

    if i % 2 == 0:
        li.append(d[i // 2])
    if i % 3 == 0:
        li.append(d[i // 3])
    if i % 5 == 0:
        li.append(d[i // 5])

    d[i] = min(li) + 1

print(d[X])