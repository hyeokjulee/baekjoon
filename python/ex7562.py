import sys
from collections import deque

n = int(sys.stdin.readline()) # 테스트 케이스의 개수
outQ = deque()

for _ in range(n):
	l = int(sys.stdin.readline()) # 체스판의 한 변의 길이
	x1, y1 = map(int, sys.stdin.readline().split()) # 나이트가 현재 있는 칸
	x2, y2 = map(int, sys.stdin.readline().split()) # 나이트가 이동하려고 하는 칸

	if x1 == x2 and y1 == y2:
		outQ.append(0)
	else:
		board = [[0 for _ in range(l)] for _ in range(l)] # 체스판

		q = deque([(x1, y1)]) # 첫 위치 들어있는 큐
		dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]] # 방향 정보 리스트

		while q: # 큐가 빌 때까지
			x, y = q.popleft() # 큐에서 현재 위치 빼기
			
			for d in dir: # 8개 방향
				rx, ry = x + d[0], y + d[1] # 다음 위치
				
				if 1 <= rx <= l and 1 <= ry <= l and board[ry - 1][rx - 1] == 0: # 체스판 안에 있고 값이 0이라면
					q.append((rx, ry)) # 큐에 다음 위치 넣기
					board[ry - 1][rx - 1] = board[y - 1][x - 1] + 1 # 다음 위치 값 = 현재 위치 값 + 1

		outQ.append(board[y2 - 1][x2 - 1])

while outQ:
	print(outQ.popleft())
