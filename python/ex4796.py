import sys

case = 0
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0:
        break
    case += 1
    d, r = divmod(V, P)
    if r > L:
        r = L
    print('Case ' + str(case) + ': ' + str(d * L + r))