import sys, heapq

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))

result = 0
for _ in range(N - 1):
    n1 = heapq.heappop(nums)
    n2 = heapq.heappop(nums)
    n3 = n1 + n2
    heapq.heappush(nums, n3)
    result += n3

print(result)