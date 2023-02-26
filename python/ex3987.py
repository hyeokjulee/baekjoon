import sys

N, M = map(int, sys.stdin.readline().split())

space = [[] for _ in range(N)]

for i in range(N):
    space[i] = list(sys.stdin.readline().rstrip('\n'))

PR, PC = map(int, sys.stdin.readline().split())

space[PR - 1][PC - 1] = 'S'

print()
for i in range(N):
    for j in range(N):
        print(space[i][j], end='')
    print()