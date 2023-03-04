import sys

N, M = map(int, sys.stdin.readline().split())
space = [[] for _ in range(N)]
for i in range(N):
    space[i] = list(sys.stdin.readline().rstrip('\n'))
PR, PC = map(int, sys.stdin.readline().split())

cntList = []

def whilefuntion(direction):
    position = [PR, PC] # 현재 위치
    firstdirection = direction
    cnt = 0
    flag = True
    while flag:
        if cnt > M * N * 2:
            print(firstdirection)
            print('Voyager')
            sys.exit(0)
        here = space[position[0] - 1][position[1] - 1]
        if direction == 'U':
            if here == 'C':
                flag = False
            elif here == '.':
                if position[0] == 1: # 위에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] -= 1 # 위로 한칸 이동
                    cnt += 1
            elif here == '/':
                direction = 'R'
                if position[1] == M: # 오른쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] += 1  # 오른쪽으로 한칸 이동
                    cnt += 1
            elif here == '\\':
                direction = 'L'
                if position[1] == 1: # 왼쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] -= 1  # 왼쪽으로 한칸 이동
                    cnt += 1
        elif direction == 'R':
            if here == 'C':
                flag = False
            elif here == '.':
                if position[1] == M: # 오른쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] += 1  # 오른쪽으로 한칸 이동
                    cnt += 1
            elif here == '/':
                direction = 'U'
                if position[0] == 1: # 위에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] -= 1 # 위로 한칸 이동
                    cnt += 1
            elif here == '\\':
                direction = 'D'
                if position[0] == N: # 아래에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] += 1  # 아래로 한칸 이동
                    cnt += 1
        elif direction == 'D':
            if here == 'C':
                flag = False
            elif here == '.':
                if position[0] == N: # 아래에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] += 1  # 아래로 한칸 이동
                    cnt += 1
            elif here == '/':
                direction = 'L'
                if position[1] == 1: # 왼쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] -= 1  # 왼쪽으로 한칸 이동
                    cnt += 1
            elif here == '\\':
                direction = 'R'
                if position[1] == M: # 오른쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] += 1  # 오른쪽으로 한칸 이동
                    cnt += 1
        elif direction == 'L':
            if here == 'C':
                flag = False
            elif here == '.':
                if position[1] == 1: # 왼쪽에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[1] -= 1  # 왼쪽으로 한칸 이동
                    cnt += 1
            elif here == '/':
                direction = 'D'
                if position[0] == N: # 아래에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] += 1  # 아래로 한칸 이동
                    cnt += 1
            elif here == '\\':
                direction = 'U'
                if position[0] == 1: # 위에 공간이 남아있지 않다면
                    cnt += 1
                    flag = False
                else:
                    position[0] -= 1 # 위로 한칸 이동
                    cnt += 1
    return cnt

cntList.append(whilefuntion('U'))
cntList.append(whilefuntion('R'))
cntList.append(whilefuntion('D'))
cntList.append(whilefuntion('L'))

m = max(cntList)
ind = cntList.index(m)
if ind == 0:
    print('U')
elif ind == 1:
    print('R')
elif ind == 2:
    print('D')
elif ind == 3:
    print('L')
print(m)