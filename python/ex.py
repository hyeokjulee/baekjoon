import sys

board = {(1, 2)}
board.add(tuple(sorted(list((2, 1)))))

print(board)