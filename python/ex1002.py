import sys, math

T = int(sys.stdin.readline())
list = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            if r1 == 0:
                list.append(1)
            else:
                list.append(-1)
        else:
            list.append(0)
    else:
        r0 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        if r0 > r1 + r2:
            list.append(0)
        elif r0 == r1 + r2:
            list.append(1)
        else:
            if r0 + r1 == r2 or r0 + r2 == r1:
                list.append(1)
            elif r0 + r1 < r2 or r0 + r2 < r1:
                list.append(0)
            else:
                list.append(2)
        
for _ in range(T):
    print(list.pop(0))