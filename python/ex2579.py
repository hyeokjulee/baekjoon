import sys

N = int(sys.stdin.readline())
scores = []

for _ in range(N):
    scores.append(int(sys.stdin.readline()))

if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
else:
    d = [scores[0], scores[0] + scores[1], max(scores[0] + scores[2], scores[1] + scores[2])] # d[0], d[1], d[2]

    for i in range(3, N):
        d.append(max(d[i - 2] + scores[i], d[i - 3] + scores[i] + scores[i - 1])) # d[3] ~ d[N - 1]

    print(d[N - 1])