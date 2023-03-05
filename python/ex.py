import sys

nums = []

for i in range(123, 988):
    num = str(i)
    if num[0] != '0' and num[1] != '0' and num[2] != '0' and num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
        nums.append(num)

for num in reversed(nums):
    print(num)