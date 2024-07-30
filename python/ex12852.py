import sys

N = int(sys.stdin.readline())

miniArr = [0, 0]
nextArr = [0, 0]
for i in range(2, N + 1):
    mini = miniArr[i - 1] + 1
    next = i - 1
    if i % 2 == 0 and mini > miniArr[i // 2] + 1:
        mini = miniArr[i // 2] + 1
        next = i // 2
    if i % 3 == 0 and mini > miniArr[i // 3] + 1:
        mini = miniArr[i // 3] + 1
        next = i // 3
    miniArr.append(mini)
    nextArr.append(next)

print(miniArr[N])
while N > 0:
    print(N, end = ' ')
    N = nextArr[N]