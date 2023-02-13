import sys

N = int(sys.stdin.readline())

a = [0, 1, 0, 2, 0] # 그해에 태어난 개체수(홀수년도)
b = [0, 0, 1, 0, 4] # 그해에 태어난 개체수(짝수년도)
d = [0, 0, 0, 0, 1] # 그해에 죽을 개체수
x = [0, 1, 2, 4, 7] # 그해 말에 존재하는 개체수

for i in range(5, N + 1): # 5년부터 N년까지 계산
    if i % 2 == 0: # i년이 짝수년이라면
        a.append(0)
        b.append(x[i - 1])
    else: # i년이 홀수년이라면
        a.append(x[i - 1])
        b.append(0)

    d.append(a[i - 3] + b[i - 4]) # 3년전 홀수년도에 태어난 개체수 + 4년전 짝수년도에 태어난 개체수
    x.append(x[i - 1] + a[i] + b[i] - d[i])
print(x[N])