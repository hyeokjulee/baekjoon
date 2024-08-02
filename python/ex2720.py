import sys

T = int(sys.stdin.readline())

coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(sys.stdin.readline())
    for coin in coins:
        print(C // coin, end=' ')
        C = C % coin
    print()
