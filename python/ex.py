import sys

l = int(sys.stdin.readline()) # 체스판의 한 변의 길이

board = [['0' * l] * l]

for i in range(l):
    for j in range(l):
        print(board[i][j], end=' ')
    print()