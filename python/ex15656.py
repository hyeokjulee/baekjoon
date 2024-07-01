import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

for i in product(numbers, repeat = M):
    print(*i)