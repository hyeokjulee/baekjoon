import sys

N, M = map(int, sys.stdin.readline().split())

space = [[] for _ in range(N)]

for i in range(N):
    space[i] = list(sys.stdin.readline().rstrip('\n'))

PR, PC = map(int, sys.stdin.readline().split())

position = [PR - 1, PC - 1]

print()
for i in range(N):
    for j in range(N):
        print(space[i][j], end='')
    print()

# 위
cnt = 0
direction = 'U'
flag = True
while flag:
    if direction == 'U':
        if position[0] != 0:
            position = [position[0] - 1][position[1]]
        if position[0] == 0 or position[0] == 'C':
            flag = False
        elif space[position[0]][position[1]] == '.':
            cnt += 1
        elif space[position[0]][position[1]] == '/':
            cnt += 1
            position = [position[0] - 1][position[1]]
            direction = 'R'
        elif space[position[0]][position[1]] == '\\':
            cnt += 1
            direction = 'L'
    if direction == 'R':


# 오른쪽
# 아래
# 왼쪽 (U: 위, R: 오른쪽, D: 아래, L: 왼쪽)