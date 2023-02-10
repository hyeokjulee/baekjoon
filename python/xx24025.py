import sys

n = int(sys.stdin.readline()) # 무리의 수 n 입력
a = list(map(int, sys.stdin.readline().split())) # 시야점수의 조건을 나타내는 배열 a 입력
o = [0 for _ in range(n)] # 정령 무리들의 키가 들어갈 리스트

y = [[0 for col in range(2)] for row in range(n)]
for i in range(n):
    y[i][0] = a[i]
    y[i][1] = i
y.sort()
y.reverse()




# 점수 처리
k = [0 for _ in range(n)] # 정령 무리들의 점수가 들어갈 리스트
maxIndexOfO = n - 1 # 마지막 정령 무리의 키가 현재 최고 키

m = [[0 for col in range(2)] for row in range(n)]
for i in range(n):
    m[i][0] = o[i]
    m[i][1] = i

for i in range(n-1,-1,-1):
    if o[i] < m[maxIndexOfO][0]:
        k[i] = m[maxIndexOfO][1] - i
    else: # 모두 볼 수 있다면
        maxIndexOfO = i
        k[i] = 1000000000

k.reverse() # 배열 요소들의 순서를 뒤집기

answer = ""
for i in range(n): # 조건 확인 후 출력
    if (a[i] < 0 and k[i] <= -a[i]) or (a[i] > 0 and k[i] >= a[i]): # 조건에 만족하면
        answer += str(o[i])
        if i < n - 1:
            answer += ' '
        else: # 정령무리들 모두 만족한 거면
            print(answer)
            sys.exit()
    else: # 조건에 만족하지 않으면
        print(-1)
        sys.exit()