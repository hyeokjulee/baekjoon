import sys

d = [[0], [1], [1, 1], [1, 2, 1], [0, 3, 3, 1]]

for i in range(5, 1001):
    arr = [0] * i
    for j in range(1, i - 2):
        arr[j] = (d[i - 1][j - 1] + d[i - 2][j - 1] + d[i - 3][j - 1]) % 1000000009
    arr[i - 2], arr[i - 1] = i - 1, 1
    d.append(arr)

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(d[n][m - 1])