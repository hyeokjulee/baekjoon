import sys

n = int(sys.stdin.readline()) # 무리의 수 n 입력
a = list(map(int, sys.stdin.readline().split())) # 시야점수의 조건을 나타내는 배열 a 입력
b = a.copy()
o = [0 for _ in range(n)] # 정령 무리들의 키가 들어갈 리스트
for i in range(n):
  if max(b) > 0:
    o[b.index(max(b))] = n - i
    b[b.index(max(b))] = 0
  else:
    o[b.index(min(b))] = n - i
    b[b.index(min(b))] = 0


# 점수 처리
k = [0 for _ in range(n)] # 정령 무리들의 점수가 들어갈 리스트
max = o[n - 1] # 마지막 정령 무리의 키가 현재 최고 키
for i in range(n-1,-1,-1):
    if o[i] < max:
        k[i] = o.index(max) - i
    else: # 모두 볼 수 있다면
        max = o[i]
        k[i] = 1000000000
    k.reverse() # 배열 요소들의 순서를 뒤집기


for i in range(n): # 조건 확인 후 출력
    if (a[i] < 0 or k[i] < a[i]) and (a[i] > 0 or k[i] > -a[i]) or a[n - 1] < 0: # 조건에 만족하지 않으면
        print(-1)
        sys.exit()
    else: # 조건에 만족하면
        if i == n - 1: # 근데 정령무리들 모두 만족한 거면
            answer = ""
            for i in range(n):
                answer += str(o[i]) + ' '
            print(answer)