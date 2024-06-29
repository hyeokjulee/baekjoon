import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] * M

def func(x):
    if x is M:
        for i in range(M):
            print(nums[i], end=" ")
        print()
    else:
        for i in range(N):
            nums[x] = i + 1
            func(x + 1)

func(0)