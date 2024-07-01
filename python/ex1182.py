import sys, copy

N, S = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

subsets_of_numbers = []
subset = []
cnt = 0

def func(n):
    if n == N:
        subsets_of_numbers.append(copy.deepcopy(subset))
    else:
        func(n + 1)
        subset.append(numbers[n])
        func(n + 1)
        subset.pop()

func(0)
subsets_of_numbers.remove([])

for i in subsets_of_numbers:
    if sum(i) == S:
        cnt += 1

print(cnt)