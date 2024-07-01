import sys

N, S = map(int, sys.stdin.readline().split())
nums = tuple(map(int, sys.stdin.readline().split()))
cnt = 0

def func(idx, sum):
    if idx < N:
        func(idx + 1, sum)
        func(idx + 1, sum + nums[idx])
    else:
        if sum == S:
            global cnt
            cnt += 1

func(0, 0)

if S != 0:
    print(cnt)
else:
    print(cnt - 1)