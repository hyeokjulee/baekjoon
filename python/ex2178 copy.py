import sys

N, M = map(int, sys.stdin.readline().split())

maze = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    maze[i] = list(map(int, sys.stdin.readline().strip()))

def mazerun(a, b, x):
    if 1 <= a <= M and 1 <= b <= N and maze[b - 1][a - 1] == 1:
        maze[b - 1][a - 1] = x

        mazerun(a - 1, b, x + 1)
        mazerun(a + 1, b, x + 1)
        mazerun(a, b - 1, x + 1)
        mazerun(a, b + 1, x + 1)

mazerun(1, 1, 1)

for i in range(N):
    print(maze[i])