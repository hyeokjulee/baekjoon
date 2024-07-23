import sys

N = int(sys.stdin.readline())
map = []
for _ in range(N):
    map.append(list(sys.stdin.readline()))

cntList = []
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    map[y][x] = 0
    if x > 0 and map[y][x - 1] == "1":
        dfs(x - 1, y)
    if x < N - 1 and map[y][x + 1] == "1":
        dfs(x + 1, y)
    if y > 0 and map[y - 1][x] == "1":
        dfs(x, y - 1)
    if y < N - 1 and map[y + 1][x] == "1":
        dfs(x, y + 1)
    
for i in range(N):
    for j in range(N):
        if map[i][j] == "1":
            cnt = 0
            dfs(j, i)
            cntList.append(cnt)

print(len(cntList))
for i in sorted(cntList):
    print(i)