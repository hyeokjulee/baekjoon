import sys, queue, copy

R, C = map(int, sys.stdin.readline().split())
space = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    space[i] = list(sys.stdin.readline())

hunSpace, fireSpace = copy.deepcopy(space), copy.deepcopy(space)
hunPositionQueue, firePositionQueue = queue.Queue(), queue.Queue()

for i in range(R):
    for j in range(C):
        if space[i][j] == 'J':
            hunSpace[i][j] = 1
            fireSpace[i][j] = '.'
            hunPosition = [j, i]
            hunPositionQueue.put(hunPosition)
        if space[i][j] == 'F':
            fireSpace[i][j] = 1
            hunSpace[i][j] = '#'
            firePosition = [j, i]
            firePositionQueue.put(firePosition)

while not firePositionQueue.empty():
    oldFirePosition = firePositionQueue.get()
    x, y = oldFirePosition[0], oldFirePosition[1]
    if x > 0 and fireSpace[y][x - 1] == ".":
        fireSpace[y][x - 1] = fireSpace[y][x] + 1
        newFirePosition = [x - 1, y]
        firePositionQueue.put(newFirePosition)
    if x < C - 1 and fireSpace[y][x + 1] == ".":
        fireSpace[y][x + 1] = fireSpace[y][x] + 1
        newFirePosition = [x + 1, y]
        firePositionQueue.put(newFirePosition)
    if y > 0 and fireSpace[y - 1][x] == ".":
        fireSpace[y - 1][x] = fireSpace[y][x] + 1
        newFirePosition = [x, y - 1]
        firePositionQueue.put(newFirePosition)
    if y < R - 1 and fireSpace[y + 1][x] == ".":
        fireSpace[y + 1][x] = fireSpace[y][x] + 1
        newFirePosition = [x, y + 1]
        firePositionQueue.put(newFirePosition)

while not hunPositionQueue.empty():
    oldHunPosition = hunPositionQueue.get()
    x, y = oldHunPosition[0], oldHunPosition[1]
    if x > 0 and hunSpace[y][x - 1] == ".":
        if fireSpace[y][x - 1] == "." or hunSpace[y][x] + 1 < fireSpace[y][x - 1]:
            hunSpace[y][x - 1] = hunSpace[y][x] + 1
            newHunPosition = [x - 1, y]
            hunPositionQueue.put(newHunPosition)
        else:
            hunSpace[y][x - 1] = "#"
    if x < C - 1 and hunSpace[y][x + 1] == ".":
        if fireSpace[y][x + 1] == "." or hunSpace[y][x] + 1 < fireSpace[y][x + 1]:
            hunSpace[y][x + 1] = hunSpace[y][x] + 1
            newHunPosition = [x + 1, y]
            hunPositionQueue.put(newHunPosition)
        else:
            hunSpace[y][x + 1] = "#"
    if y > 0 and hunSpace[y - 1][x] == ".":
        if fireSpace[y - 1][x] == "." or hunSpace[y][x] + 1 < fireSpace[y - 1][x]:
            hunSpace[y - 1][x] = hunSpace[y][x] + 1
            newHunPosition = [x, y - 1]
            hunPositionQueue.put(newHunPosition)
        else:
            hunSpace[y - 1][x] = "#"
    if y < R - 1 and hunSpace[y + 1][x] == ".":
        if fireSpace[y + 1][x] == "." or hunSpace[y][x] + 1 < fireSpace[y + 1][x]:
            hunSpace[y + 1][x] = hunSpace[y][x] + 1
            newHunPosition = [x, y + 1]
            hunPositionQueue.put(newHunPosition)
        else:
            hunSpace[y + 1][x] = "#"

minTime = -1
for i in range(R):
    for j in range(C):
        if (j == 0 or j == C - 1 or i == 0 or i == R - 1) and type(hunSpace[i][j]) is int and (minTime == -1 or hunSpace[i][j] < minTime):
                minTime = hunSpace[i][j]

if not minTime == -1:
    print(minTime)
else:
    print('IMPOSSIBLE')