import sys

N = int(sys.stdin.readline())
cities = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

def binary_search():
    start = 0
    end = max(cities)
    res = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for city in cities:
            if city < mid:
                total += city
            else:
                total += mid
            
        if total > M:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    print(res)

binary_search()