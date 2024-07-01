import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

for i in combinations(numbers, M):
    print(*i)