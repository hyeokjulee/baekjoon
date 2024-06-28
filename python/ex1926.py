import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

paper = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    paper[i] = list(map(int, sys.stdin.readline().split()))

areaSet = {0}
cnt = 0

def bfs(x, y):
    global area
    area += 1
    paper[y][x] = 0
    if x > 0 and paper[y][x - 1] == 1:
        bfs(x - 1, y)
    if x < M - 1 and paper[y][x + 1] == 1:
        bfs(x + 1, y)
    if y > 0 and paper[y - 1][x] == 1:
        bfs(x, y - 1)
    if y < N - 1 and paper[y + 1][x] == 1:
        bfs(x, y + 1)
    
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            area = 0
            bfs(j, i)
            if area != 0:
                cnt += 1
                areaSet.add(area)

print(cnt)
print(max(areaSet))