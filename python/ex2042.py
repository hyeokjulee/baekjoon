import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = [0] * (N + 1)
tree = [0] * (N + 1)

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += i & (-i)
        
def sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= i & (-i)
    return result

for i in range(1, N + 1):
    x = int(sys.stdin.readline())
    arr[i] = x
    update(i, x)
    
for _ in range( M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 1:
        diff = c - arr[b]
        update(b, diff)
    else:
        print(sum(c) - sum(b - 1))