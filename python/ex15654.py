import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] * M
is_used = [False] * N
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

def func(x):
    if x == M:
        for i in range(M):
            print(numbers[nums[i]], end=" ")
        print()
    else:
        for i in range(N):
            if not is_used[i]:
                nums[x] = i
                is_used[i] = True
                func(x + 1)
                is_used[i] = False

func(0)