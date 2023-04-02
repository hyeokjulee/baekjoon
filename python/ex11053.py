import sys, copy

N = int(sys.stdin.readline())
inLi = list(map(int, sys.stdin.readline().split()))
outLi = [[inLi[0]]]

for i in range(1, N):
    liLi = copy.deepcopy(outLi)
    l = len(liLi)
    for j in range(l - 1, -1, -1):
        if liLi[j][-1] >= inLi[i]:
            del liLi[j]
    if liLi:
        temp = max(liLi, key=len)
        temp.append(inLi[i])
        outLi.append(temp)
print(len(max(outLi, key=len)))
# 붙일 수 있는(마지막원소가 현재숫자보다 작은) 배열중 가장 긴(len이 가장 큰)배열에 붙이기
# 배열을 복사해서 사본에서 마지막원소가 현재숫자이상인 수들을 빼고 가장 긴 배열을 골라 끝에 수를 붙임
