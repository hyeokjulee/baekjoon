import sys

T = int(sys.stdin.readline())
li = []

for _ in range(T):
    li.append(int(sys.stdin.readline()))

d0 = [1, 0]
d1 = [0, 1]

for i in range(2, max(li) + 1):
    d0.append(d0[i - 1] + d0[i - 2]) # d0[i]
    d1.append(d1[i - 1] + d1[i - 2]) # d1[i]

for i in range(T):
    print(d0[li[i]], d1[li[i]])
    