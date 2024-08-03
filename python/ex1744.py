import sys

N = int(sys.stdin.readline())
pos, neg = [], []
zer = 0
result = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        zer += 1
    elif num == 1:
        result += 1
    elif num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
pos.sort()
neg.sort()

while len(pos) >= 2:
    n1 = pos.pop()
    n2 = pos.pop()
    result += n1 * n2

if pos:
    result += pos.pop()

while len(neg) >= 2:
    n1 = neg.pop(0)
    n2 = neg.pop(0)
    result += n1 * n2
    
if neg and zer == 0:
    result += neg.pop()

print(result)