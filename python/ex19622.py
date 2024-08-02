import sys

N = int(sys.stdin.readline())
K = []
for _ in range(N):
    K.append(int(sys.stdin.readline().split()[2]))

if N >= 2:
    K[1] = max(K[1], K[0])
    for i in range(2, N):
        K[i] = max(K[i] + K[i - 2], K[i - 1])

print(K[-1])