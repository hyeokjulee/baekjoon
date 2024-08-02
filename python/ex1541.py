import sys

o = sys.stdin.readline()

m = o.split('-')

s = sum(map(int, m[0].split('+')))
for i in range(1, len(m)):
    s -= sum(map(int, m[i].split('+')))

print(s)