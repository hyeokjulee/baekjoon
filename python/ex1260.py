import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append([])
    
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A - 1].append(B)
    graph[B - 1].append(A)

visited = [False] * N

def dfs(node):
    print(node, end=' ')
    visited[node - 1] = True

    for node2 in sorted(graph[node - 1]):
        if not visited[node2 - 1]:
            dfs(node2)

dfs(V)

print()

visited = [False] * N

def bfs(node):
    q = deque([node])
    visited[node - 1] = True

    while q:
        node2 = q.popleft()
        print(node2, end=' ')

        for node3 in sorted(graph[node2 - 1]):
            if not visited[node3 - 1]:
                q.append(node3)
                visited[node3 - 1] = True

bfs(V)