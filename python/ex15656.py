import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] * M
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

def func(x):
    if x == M:
        for i in range(M):
            print(numbers[nums[i]], end=" ")
        print()
    else:
        for i in range(N):
            nums[x] = i
            func(x + 1)

func(0)