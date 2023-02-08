import sys

N = int(sys.stdin.readline()) # 돌의 정령 무리의 수
A = list(map(int, sys.stdin.readline().split())) # 시야점수의 제한 리스트

X = [0 for _ in range(N)] # 정령 무리들의 키 리스트

num = [0 for _ in range(N)] # 1부터 N까지 오름차순으로 차례대로 들어있는 리스트
for i in range(N):
    num[i] = i + 1

for i in range(N):
    if A[i] > 0: # 시야점수 제한이 양수라면
        X[i] = num.pop() # N부터 내림차순으로 차례대로 넣기
        
for i in range(N):
    if A[i] < 0: # 시야점수 제한이 음수라면
        X[i] = num.pop(0) # 1부터 오름차순으로 차례대로 넣기

if (A[N - 1]>0): # 조건에 만족하면
    answer = "" # 출력할 문자열
    for i in range(N):
        answer += str(X[i]) + ' '
    print(answer) # 문자열 출력
else: # 조건에 만족하지 않으면
    print(-1) # -1 출력