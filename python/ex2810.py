import sys

N = int(sys.stdin.readline())
I = sys.stdin.readline()

s, ll = I.count('S'), I.count('LL')

if ll:
    print(s + ll + 1)
else:
    print(s)