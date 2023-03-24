import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    for j in range(i):
        if nums[j] > nums[i]:
            nums.insert(j, nums.pop(i))
            break

for num in nums:
    print(num, end=" ")