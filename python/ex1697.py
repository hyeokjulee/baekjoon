import sys, queue

N, K = map(int, sys.stdin.readline().split())
lengthOfLine = 2 * max(N, K)
line = [lengthOfLine for _ in range(lengthOfLine)]
line[N] = 0
binPositionQueue = queue.Queue()
binPositionQueue.put(N)

while not binPositionQueue.empty():
    x = binPositionQueue.get()
    if x > 0 and line[x] + 1 < line[x - 1]:
        line[x - 1] = line[x] + 1
        newBinPosition = x - 1
        binPositionQueue.put(newBinPosition)
    if x < lengthOfLine - 1 and line[x] + 1 < line[x + 1]:
        line[x + 1] = line[x] + 1
        newBinPosition = x + 1
        binPositionQueue.put(newBinPosition)
    if x < lengthOfLine // 2 and line[x] + 1 < line[2 * x]:
        line[2 * x] = line[x] + 1
        newBinPosition = 2 * x
        binPositionQueue.put(newBinPosition)

print(line[K])