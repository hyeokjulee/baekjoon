import sys

K , N = map(int, sys.stdin.readline().split())
lans = []
for _ in range(K):
    lans.append(int(sys.stdin.readline()))
    
start = 1
end = max(lans)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt < N:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)