import sys

answer = "" # 출력할 문자열
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())

    A = [[0 for col in range(N)] for row in range(2)] # 지원자 성적 순위 리스트

    for j in range(0, N):
        A[0][j], A[1][j] = sys.stdin.readline().split()
        A[0][j] = int(A[0][j])
        A[1][j] = int(A[1][j])
        
    A0 = A[0][A[1].index(1)]
    A1 = A[1][A[0].index(1)]

    for j in range(len(A[0]) - 1, -1, -1):
        if A[0][j] > A0:
            del A[0][j]
            del A[1][j]

    for j in range(len(A[0]) - 1, -1, -1):
        if A[1][j] > A1:
            del A[0][j]
            del A[1][j]


    
    applicant = [[0 for col in range(2)] for row in range(len(A[0]))] # 선발 가능 인원 리스트
    for j in range(2):
        for k in range(len(A[0])):
            applicant[k][j] = A[j][k]
    passed = [applicant[0]]
    fail = [] # passed에서 뺄 인덱스값들의 리스트

    for j in range(1, len(applicant)):
        if applicant[j][0] < max([k[0] for k in passed]) or applicant[j][1] < max([k[1] for k in passed]): # 최대값보다 낮은 숫자가 하나라도 있으면
            for k in range(len(passed)):
                if applicant[j][0] < passed[k][0] and applicant[j][1] < passed[k][1]: # 추가한 지금 지원자와 비교하여 둘다 높으면 
                    fail.append(k) # 버림 리스트에 추가

            for k in range(len(fail)):
                del passed[fail.pop()] # 버림

            passed.append(applicant[j]) # 선발 가능 인원 리스트에 지원자 추가


    answer += str(len(passed)) + '\n'
print(answer)