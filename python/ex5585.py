import sys

money = 1000 - int(sys.stdin.readline())
num = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    num += money // coin
    money = money % coin

print(num)