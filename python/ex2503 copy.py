import sys

outList = []
for i in range(123, 988):
    if str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2]:
        outList.append(str(i)) # 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수 일단 모두 넣어 놓기

for _ in range(int(sys.stdin.readline())):
    num, s, b = map(str, sys.stdin.readline().split())

    if s == '3':
        print(1)
        sys.exit()

    if s == '2':
        for i in range(len(outList) - 1, -1, -1):
            if not(outList[i][0] == num[0] and outList[i][1] == num[1] and outList[i][2] != num[2] or outList[i][0] == num[0] and outList[i][1] != num[1] and outList[i][2] == num[2] or outList[i][0] != num[0] and outList[i][1] == num[1] and outList[i][2] == num[2]):
                del outList[i]

    if s == '1' and b == '2':
        for i in range(len(outList) - 1, -1, -1):
            if not(outList[i][0] == num[0] and outList[i][1] != num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] == num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] != num[1] and outList[i][2] == num[2]):
                if num[0] in outList[i] and num[1] in outList[i] and num[2] not in outList[i] or num[0] in outList[i] and num[1] not in outList[i] and num[2] in outList[i] or num[0] not in outList[i] and num[1] in outList[i] and num[2] in outList[i]:
                    del outList[i]

    if s == '1' and b == '1':
        for i in range(len(outList) - 1, -1, -1):
            if not(outList[i][0] == num[0] and outList[i][1] != num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] == num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] != num[1] and outList[i][2] == num[2]):
                if num[0] in outList[i] and num[1] not in outList[i] and num[2] not in outList[i] or num[0] not in outList[i] and num[1] not in outList[i] and num[2] in outList[i] or num[0] not in outList[i] and num[1] in outList[i] and num[2] not in outList[i]:
                    del outList[i]

    if s == '1' and b == '0':
        for i in range(len(outList) - 1, -1, -1):
            if not(outList[i][0] == num[0] and outList[i][1] != num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] == num[1] and outList[i][2] != num[2] or outList[i][0] != num[0] and outList[i][1] != num[1] and outList[i][2] == num[2]):
                if num[0] in outList[i] or num[1] in outList[i] or num[2] in outList[i]:
                    del outList[i]

    if s == '0' and b == '3':
        for i in range(len(outList) - 1, -1, -1):
            if outList[i][0] == num[0] or outList[i][1] == num[1] or outList[i][2] == num[2]:
                if not(num[0] in outList[i] and num[1] in outList[i] and num[2] in outList[i]):
                    del outList[i]

    if s == '0' and b == '2':
        for i in range(len(outList) - 1, -1, -1):
            if outList[i][0] == num[0] or outList[i][1] == num[1] or outList[i][2] == num[2]:
                if num[0] in outList[i] and num[1] in outList[i] and num[2] not in outList[i] or num[0] in outList[i] and num[1] not in outList[i] and num[2] in outList[i] or num[0] not in outList[i] and num[1] in outList[i] and num[2] in outList[i]:
                    del outList[i]

    if s == '0' and b == '1':
        for i in range(len(outList) - 1, -1, -1):
            if outList[i][0] == num[0] or outList[i][1] == num[1] or outList[i][2] == num[2]:
                if num[0] in outList[i] and num[1] not in outList[i] and num[2] not in outList[i] or num[0] not in outList[i] and num[1] not in outList[i] and num[2] in outList[i] or num[0] not in outList[i] and num[1] in outList[i] and num[2] not in outList[i]:
                    del outList[i]

    if s == '0' and b == '0':
        for i in range(len(outList) - 1, -1, -1):
            if outList[i][0] == num[0] or outList[i][1] == num[1] or outList[i][2] == num[2]:
                if num[0] in outList[i] or num[1] in outList[i] or num[2] in outList[i]:
                    del outList[i]

print(len(outList))