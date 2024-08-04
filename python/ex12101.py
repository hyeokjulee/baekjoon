import sys

way_set_list = [set(), {'1'}]
n, k = map(int, sys.stdin.readline().split())

for i in range(2, 11):
    way_set_list.append(set())
    for pre_way in way_set_list[i - 1]:
        way_list = list(map(int, pre_way.split('+')))
        
        for j in range(len(way_list) + 1):
            way_list.insert(j, 1)
            way_set_list[i].add('+'.join(map(str, way_list)))
            way_list.pop(j)

        for j in range(len(way_list)):
            if way_list[j] < 3:
                way_list[j] += 1
                way_set_list[i].add('+'.join(map(str, way_list)))
                way_list[j] -= 1

sorted_way_list = sorted(way_set_list[n])

if k > len(sorted_way_list):
    print(-1)
else:
    print(sorted_way_list[k - 1])