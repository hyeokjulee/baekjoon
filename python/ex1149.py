import sys

rgb_cost = []
N = int(sys.stdin.readline())
for _ in range(N):
    rgb_cost.append(list(map(int, sys.stdin.readline().split())))

total_cost = [rgb_cost[0]]
for i in range(1, N):
    r = rgb_cost[i][0] + min(total_cost[i-1][1], total_cost[i-1][2])
    g = rgb_cost[i][1] + min(total_cost[i-1][0], total_cost[i-1][2])
    b = rgb_cost[i][2] + min(total_cost[i-1][0], total_cost[i-1][1])
    total_cost.append([r, g, b])

print(min(total_cost[-1]))