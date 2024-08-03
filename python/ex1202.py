import sys, heapq

jewel  = []
bag = []
tmp = []
result = 0
N, K = map(int, sys.stdin.readline().split())
jewel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]
jewel.sort()
bag.sort()

for b in bag:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(tmp, -jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        result -= heapq.heappop(tmp)
    
print(result)