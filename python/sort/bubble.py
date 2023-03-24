import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(num, end=" ")