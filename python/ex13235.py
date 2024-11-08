import sys

str = sys.stdin.readline().rstrip()
LengthOfStr = len(str)

for i in range(int(LengthOfStr / 2)):
    if not str[i] is str[LengthOfStr - i - 1]:
        print('false')
        exit(0)

print('true')