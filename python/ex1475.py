import sys, math
N = sys.stdin.readline()
print(int(max([N.count('0'), N.count('1'), N.count('2'), N.count('3'), N.count('4'), N.count('4'), N.count('5'), math.ceil((N.count('6') + N.count('9')) / 2), N.count('7'), N.count('8')])))