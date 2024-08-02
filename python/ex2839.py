import sys

N = int(sys.stdin.readline())

d1 = N // 5
r1 = N % 5

while d1 >= 0:
    d2 = r1 // 3
    r2 = r1 % 3

    if r2 == 0:
        print(d1 + d2)
        exit(0)

    d1 -= 1
    r1 += 5

print(-1)