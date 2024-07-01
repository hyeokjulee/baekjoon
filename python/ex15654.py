import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

for i in permutations(numbers, M):
    print(*i)