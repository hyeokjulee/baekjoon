import sys

N = int(sys.stdin.readline())

alpList = [] # 문자열들
placeValue = [] # 문자열들의 남은 자릿값들
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 알파벳에 넣어줄 숫자들
numList2 = [] # 보류중인 숫자들
for i in range(N):
    input_alp = sys.stdin.readline().rstrip('\n') # 문자열 입력
    alpList.append(input_alp)
    placeValue.append(len(input_alp))

if N < 10:
    while max(placeValue) > 0:
        mpvi = placeValue.index(max(placeValue)) # 현재 남은 자릿값이 가장 높은 문자열의 인덱스값
        if '0' <= alpList[mpvi][len(alpList[mpvi])-placeValue[mpvi]] <= '9': # 가장 높은 자릿값을 갖고있는 문자열의 첫글자가 숫자로 변해있다면
            placeValue[mpvi] -= 1 # 그 문자열의 자릿값을 1 줄이고 while문 반복하러 감
        else:
            a = alpList[mpvi][len(alpList[mpvi])-placeValue[mpvi]] # 가장 높은 자릿값을 갖고있는 문자열의 첫글자
            num = numList.pop() # 그 글자에 넣어줄 숫자
            for j in range(N):
                alpList[j] = alpList[j].replace(a, num)
else:
    while max(placeValue) > 0:
        mpvi = placeValue.index(max(placeValue)) # 현재 남은 자릿값이 가장 높은 문자열의 인덱스값
        if '0' <= alpList[mpvi][len(alpList[mpvi])-placeValue[mpvi]] <= '9': # 가장 높은 자릿값을 갖고있는 문자열의 첫글자가 숫자로 변해있다면
            placeValue[mpvi] -= 1 # 그 문자열의 자릿값을 1 줄이고 while문 반복하러 감
        else:
            if

sum = 0
for i in range(N):
    sum += int(alpList[i])
print(sum)