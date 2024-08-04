import sys

arr = [[], [], [], [], [[1, 0, 0], [0, 1, 0], [1, 1, 1], [2, 0, 1]]]

for i in range(5, 100001):
    t1 = arr[i - 1][1]
    t2 = arr[i - 1][2]
    t3 = arr[i - 1][3]
    t4 = [(t3[1] + t3[2]) % 1000000009, (t2[0] + t2[2]) % 1000000009, (t1[0] + t1[1]) % 1000000009]
    arr.append([t1, t2, t3, t4])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n < 3:
        print(1)
    elif n == 3:
        print(3)
    else:
        print(sum(arr[n][3]) % 1000000009)