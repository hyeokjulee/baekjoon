import sys

N, S = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
sums = []
sum = 0
cnt = 0

def func(n):
    global sum
    if n == N:
        sums.append(sum)
    else:
        func(n + 1)
        sum += nums[n]
        func(n + 1)
        sum -= nums[n]

func(0)

for i in sums:
    if i == S:
        cnt += 1

if S != 0:
    print(cnt)
else:
    print(cnt - 1)