import sys, queue

M, N = map(int, sys.stdin.readline().split())

box = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    box[i] = list(map(int, sys.stdin.readline().split()))

ripeQueue = queue.Queue()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripeTomato = [j, i]
            ripeQueue.put(ripeTomato)

while not ripeQueue.empty():
    oldTomato = ripeQueue.get()
    x = oldTomato[0]
    y = oldTomato[1]
    if x > 0 and box[y][x - 1] == 0:
        box[y][x - 1] = box[y][x] + 1
        newTomato = [x - 1, y]
        ripeQueue.put(newTomato)
    if x < M - 1 and box[y][x + 1] == 0:
        box[y][x + 1] = box[y][x] + 1
        newTomato = [x + 1, y]
        ripeQueue.put(newTomato)
    if y > 0 and box[y - 1][x] == 0:
        box[y - 1][x] = box[y][x] + 1
        newTomato = [x, y - 1]
        ripeQueue.put(newTomato)
    if y < N - 1 and box[y + 1][x] == 0:
        box[y + 1][x] = box[y][x] + 1
        newTomato = [x, y + 1]
        ripeQueue.put(newTomato)

flag = False
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            flag = True
if flag:
    print(-1)
    exit(0)

print(box[oldTomato[1]][oldTomato[0]] - 1)