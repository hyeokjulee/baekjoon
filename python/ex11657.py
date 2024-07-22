import sys, math

N, M = map(int, sys.stdin.readline().split())

dist = [math.inf] * (N + 1)
bus = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    bus.append((A, B, C))

dist[1] = 0

for i in range(N):
    for A, B, C in bus:
        if dist[A] != math.inf and dist[A] + C < dist[B]:
            dist[B] = dist[A] + C

            if i == N - 1:
                print(-1)
                sys.exit()

for i in range(2, N + 1):
    if dist[i] == math.inf:
        print(-1)
    else:
        print(dist[i])