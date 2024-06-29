import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
print_set = set()
nums = [0] * N
is_used = [False] * N

def func(x):
    if x == M:
        temp = []
        for i in range(M):
            temp.append(numbers[nums[i]])
        print_set.add(tuple(temp))
    else:
        for i in range(N):
            if not is_used[i] and (x == 0 or i >= nums[x - 1]):
                nums[x] = i
                is_used[i] = True
                func(x + 1)
                is_used[i] = False

func(0)

for i in sorted(print_set):
    print(' '.join(map(str, i)))