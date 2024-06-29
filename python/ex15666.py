import sys

N, M = map(int, sys.stdin.readline().split())
input_numbers = set(map(int, sys.stdin.readline().split()))
numbers = sorted(input_numbers)
L = len(numbers)
nums = [0] * M

def func(m):
    if m == M:
        for i in range(M):
            print(numbers[nums[i]], end=' ')
        print()
        return
    else:
        for i in range(L):
            if m == 0 or i >= nums[m - 1]:
                nums[m] = i
                func(m + 1)

func(0)