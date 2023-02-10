import sys

N, K, A, B = map(int, sys.stdin.readline().split())

x = K
cnt = 0
while x > 0:
    cnt += 1
    if cnt % (N / A) == 0:
        x += B
    x -= 1
print(cnt)