import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())

for i in combinations_with_replacement([_ for _ in range(1, N + 1)], M):
    print(*i)