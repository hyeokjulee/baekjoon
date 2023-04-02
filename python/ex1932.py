import sys

n = int(sys.stdin.readline())

li = []

for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    li[i][0] += li[i - 1][0]
    li[i][i] += li[i - 1][i - 1]
    
for i in range(2, n):
    for j in range(1, i):
        li[i][j] += max(li[i - 1][j - 1], li[i - 1][j])

print(max(li[n - 1]))