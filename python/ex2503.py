import sys

nums = []

for i in range(123, 988): # 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수 일단 모두 넣어 놓기
    num = str(i)
    if num[0] != '0' and num[1] != '0' and num[2] != '0' and num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
        nums.append(num)

for _ in range(int(sys.stdin.readline())):
    no, strike, ball = map(int, sys.stdin.readline().split())
    no = str(no)

    for num in reversed(nums):
        cnt = 0 # 스트라이크 수 체크
        if no[0] == num[0]:
            cnt += 1
        if no[1] == num[1]:
            cnt += 1
        if no[2] == num[2]:
            cnt += 1
        if strike != cnt:
            nums.remove(num)
            continue
        cnt = 0 # 볼 수 체크
        if no[0] == num[1]:
            cnt += 1
        if no[0] == num[2]:
            cnt += 1
        if no[1] == num[0]:
            cnt += 1
        if no[1] == num[2]:
            cnt += 1
        if no[2] == num[0]:
            cnt += 1
        if no[2] == num[1]:
            cnt += 1
        if ball != cnt:
            nums.remove(num)

print(len(nums))