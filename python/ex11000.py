import sys, heapq

times = []
N = int(sys.stdin.readline())
for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().split())))
times.sort()

h = [0]
for t in times:
    if t[0] >= h[0]:
        heapq.heappop(h)
    heapq.heappush(h, t[1])

print(len(h))