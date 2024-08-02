import sys, bisect

N = int(sys.stdin.readline())
K = []
for _ in range(N):
    K.append(list(map(int, sys.stdin.readline().split())))

K.sort(key = lambda x : x[1])

Ke = []
for i in range(N):
    Ke.append(K[i][1])

for i in range(1, N):
    idx = bisect.bisect_left(Ke, K[i][0])
    if idx == 0:
        K[i][2] = max(K[i][2], K[i - 1][2])
    else:
        K[i][2] = max(K[i][2] + K[idx - 1][2], K[i - 1][2])

print(K[-1][2])