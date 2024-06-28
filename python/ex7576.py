import sys, copy

M, N = map(int, sys.stdin.readline().split())

box = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    box[i] = list(map(int, sys.stdin.readline().split()))

ripeList = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe = [j, i]
            ripeList.append(ripe)

day = -1
flag = True
while flag:
    flag = False
    day += 1
    copyRipeList = copy.deepcopy(ripeList)
    ripeList.clear()
    for ripe in copyRipeList:
        x = ripe[0]
        y = ripe[1]
        if x > 0 and box[y][x - 1] == 0:
            box[y][x - 1] = 1
            flag = True
            ripe = [x - 1, y]
            ripeList.append(ripe)
        if x < M - 1 and box[y][x + 1] == 0:
            box[y][x + 1] = 1
            flag = True
            ripe = [x + 1, y]
            ripeList.append(ripe)
        if y > 0 and box[y - 1][x] == 0:
            box[y - 1][x] = 1
            flag = True
            ripe = [x, y - 1]
            ripeList.append(ripe)
        if y < N - 1 and box[y + 1][x] == 0:
            box[y + 1][x] = 1
            flag = True
            ripe = [x, y + 1]
            ripeList.append(ripe)

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            flag = True
if flag:
    print(-1)
    exit(0)

print(day)