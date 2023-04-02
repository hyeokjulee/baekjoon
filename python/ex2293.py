import sys

n, k = map(int, sys.stdin.readline().split())
coins = [] # 동전값리스트
for _ in range(n):
    val = int(sys.stdin.readline())
    if val <= k: # k원 이하의 동전들만 취급
        coins.append(val)
coins.sort() # 동전값리스트 오름차순정렬

dp = [set()] # dp테이블 : 0번 인덱스값은 빈셋을 넣어줌
for _ in range(k):
    dp.append(set()) # dp테이블은 일단 빈 셋으로 채워놓아줌 : dp[가치의합] = 조건을 충족하는 튜플들의 셋 (튜플들은 오름차순정렬해서 넣어야함)

for i in range(1, k + 1):
    for coin in coins:
        if coin == i: # 인덱스와 동전값이 같은 경우에
            dp[i].add((coin,)) # 동전값만 들어있는 튜플을 셋에넣음
        elif coin < i: # 지금인덱스보다 작은 동전값들의 경우에
            for tup in dp[i - coin]: # 각각 동전값들을 뺀 가격인덱스의 튜플들을 가져오고
                dp[i].add(tuple(sorted(list(tup + (coin,))))) # 가져온 튜플들에 동전값을 추가한 후 오름차순정렬해서 셋에 넣음
    print(i, ' : ', len(dp[i]))

print(len(dp[k]))