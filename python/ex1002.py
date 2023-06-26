import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            if r1 == 0:
                print(1)
            else:
                print(-1)
        else:
            print(0)
    else:
        r0 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if r0 > r1 + r2:
            print(0)
        elif r0 == r1 + r2:
            print(1)
        else:
            if r0 + r1 == r2 or r0 + r2 == r1:
                print(1)
            elif r0 + r1 < r2 or r0 + r2 < r1:
                print(0)
            else:
                print(2)