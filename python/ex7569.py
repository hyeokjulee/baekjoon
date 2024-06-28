import sys, queue

M, N, H = map(int, sys.stdin.readline().split())

box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        box[i][j] = list(map(int, sys.stdin.readline().split()))

ripeQueue = queue.Queue()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                ripeTomato = [k, j, i]
                ripeQueue.put(ripeTomato)

while not ripeQueue.empty():
    oldTomato = ripeQueue.get()
    x = oldTomato[0]
    y = oldTomato[1]
    z = oldTomato[2]
    if x > 0 and box[z][y][x - 1] == 0:
        box[z][y][x - 1] = box[z][y][x] + 1
        newTomato = [x - 1, y, z]
        ripeQueue.put(newTomato)
    if x < M - 1 and box[z][y][x + 1] == 0:
        box[z][y][x + 1] = box[z][y][x] + 1
        newTomato = [x + 1, y, z]
        ripeQueue.put(newTomato)
    if y > 0 and box[z][y - 1][x] == 0:
        box[z][y - 1][x] = box[z][y][x] + 1
        newTomato = [x, y - 1, z]
        ripeQueue.put(newTomato)
    if y < N - 1 and box[z][y + 1][x] == 0:
        box[z][y + 1][x] = box[z][y][x] + 1
        newTomato = [x, y + 1, z]
        ripeQueue.put(newTomato)
    if z > 0 and box[z - 1][y][x] == 0:
        box[z - 1][y][x] = box[z][y][x] + 1
        newTomato = [x, y, z - 1]
        ripeQueue.put(newTomato)
    if z < H - 1 and box[z + 1][y][x] == 0:
        box[z + 1][y][x] = box[z][y][x] + 1
        newTomato = [x, y, z + 1]
        ripeQueue.put(newTomato)

flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag = True
if flag:
    print(-1)
    exit(0)

print(box[oldTomato[2]][oldTomato[1]][oldTomato[0]] - 1)