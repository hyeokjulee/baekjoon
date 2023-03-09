import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # 미로 크기 입력

maze = []
for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip()))) # 미로 정보 입력

q = deque([(1, 1)]) # 첫 위치 들어있는 큐
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 방향 정보 리스트

while q: # 큐가 빌 때까지
	x, y = q.popleft() # 큐에서 현재 위치 빼기
	
	for d in dir: # 1보 전진 * 4 (상하좌우)
		rx, ry = x + d[0], y + d[1] # 다음 위치
		
		if 1 <= rx <= M and 1 <= ry <= N and maze[ry - 1][rx - 1] == 1: # 미로 안에 있고 값이 1이라면 (첫 위치는 재방문하지만 상관없으므로 진행)
			q.append((rx, ry)) # 큐에 다음 위치 넣기
			maze[ry - 1][rx - 1] = maze[y - 1][x - 1] + 1 # 다음 위치 값 = 현재 위치 값 + 1

print(maze[N-1][M-1])