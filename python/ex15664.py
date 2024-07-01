import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
print_set = set()

for i in combinations(numbers, M):
    print_set.add(i)

for i in sorted(print_set):
    print(*i)