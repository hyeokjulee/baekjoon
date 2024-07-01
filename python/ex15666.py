import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(set(map(int, sys.stdin.readline().split())))

for i in combinations_with_replacement(numbers, M):
    print(*i)