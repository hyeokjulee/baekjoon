import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

outList = []

for i in range(len(nums)):
    m = min(nums)
    outList.append(m)
    nums.remove(m)

print(outList)