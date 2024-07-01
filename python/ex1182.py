import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
numbers = tuple(map(int, sys.stdin.readline().split()))
cnt = 0

# for i in range(1, N + 1):
#     for j in combinations(numbers, i):
#         if sum(j) == S:
#             cnt += 1
# print(cnt)

def func(idx, sum):
    if idx < N:
        func(idx + 1, sum)
        func(idx + 1, sum + numbers[idx])
    else:
        if sum == S:
            global cnt
            cnt += 1
func(0, 0)
if S != 0:
    print(cnt)
else:
    print(cnt - 1)