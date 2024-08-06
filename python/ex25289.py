import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

max_list = []
d_dict = {}
for i in range(-99, 100):
    for a in range(1, 101):
        d_dict[a] = 0
    for a in A:
        if 1 <= a - i <= 100:
            d_dict[a] = d_dict[a - i] + 1
        else:
            d_dict[a] = 1
    max_list.append(max(d_dict.values()))
    d_dict.clear()

print(max(max_list))