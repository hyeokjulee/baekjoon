import sys

N, M = map(int, sys.stdin.readline().split())

maze = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    maze[i] = list(map(int, sys.stdin.readline().strip()))
