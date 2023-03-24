import sys
from collections import deque

n = int(sys.stdin.readline()) # 테스트 케이스의 개수
outQ = deque() # 출력할 값들 넣어놓을 큐

def bfs():
	l = int(sys.stdin.readline()) # 체스판의 한 변의 길이
	x1, y1 = map(int, sys.stdin.readline().split()) # 나이트가 현재 있는 칸
	x2, y2 = map(int, sys.stdin.readline().split()) # 나이트가 이동하려고 하는 칸

	if x1 == x2 and y1 == y2: # 이동을 하지 않는다면
		return 0
	else:
		board = [[0 for _ in range(l)] for _ in range(l)] # 체스판 (l * l)

		q = deque([(x1, y1)]) # 첫 위치 들어있는 큐
		dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]] # 방향 정보 리스트 (8개)

		while q: # 큐가 빌 때까지
			x, y = q.popleft() # 큐에서 현재 위치 빼기
			
			for d in dir: # 8개 방향
				rx, ry = x + d[0], y + d[1] # 다음 위치
				
				if rx == x2 and ry == y2: # 다음 위치가 목적지라면
					return board[y][x] + 1

				if 0 <= rx <= l - 1 and 0 <= ry <= l - 1 and board[ry][rx] == 0: # 체스판 안에 있고 값이 0이라면
					q.append((rx, ry)) # 큐에 다음 위치 넣기
					board[ry][rx] = board[y][x] + 1 # 다음 위치 값 = 현재 위치 값 + 1

for _ in range(n):
	outQ.append(bfs())

while outQ: # 큐가 빌 때까지
	print(outQ.popleft()) # 큐에 들어있는 값들 모두 출력