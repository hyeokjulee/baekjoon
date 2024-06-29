import sys

N, M = map(int, sys.stdin.readline().split())

nums = [0] * M
is_used = [False] * N

def func(x):
    if x == M:
        for i in range(M):
            print(nums[i], end=" ")
        print()
        return
    for i in range(N):
        if not is_used[i]:
            nums[x] = i + 1
            is_used[i] = True
            func(x + 1)
            is_used[i] = False

func(0)