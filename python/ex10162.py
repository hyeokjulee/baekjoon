import sys

T = int(sys.stdin.readline())

R = ''
for t in [300, 60, 10]:
    R += str(T // t) + ' '
    T %= t

if T:
    print(-1)
else:
    print(R)