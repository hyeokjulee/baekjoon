import sys

N = int(sys.stdin.readline()) # 단어의 개수

drows = [] # 입력받은 후 거꾸로 된 단어 list
alp = [] # 입력받은 단어들에 존재하는 알파벳 list

for _ in range(N):
    drow = sys.stdin.readline().rstrip('\n')[::-1] # 입력 받은 단어 거꾸로
    drows.append(drow) # drows에 저장
    for i in range(len(drow)):
        if not(drow[i] in alp): # 처음 보는 알파벳이라면
            alp.append(drow[i]) # alp에 저장

score = [0 for _ in range(len(alp))] # alp에 들어있는 알파벳 각각의 점수들 0으로 초기화

for i in range(N): # N개의 단어들
    for j in range(len(drows[i])): # 한 단어의 글자수
        for k in range(len(alp)): # 저장된 알파벳수
            if drows[i][j] == alp[k]:
                score[k] += 10 ** j 

sum = 0
score.sort(reverse=True) # 점수가 높은 것 부터 내림차순 정렬
for i in range(len(score)):
    sum += score[i] * (9 - i)
print(sum)