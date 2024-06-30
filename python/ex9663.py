import sys

N = int(sys.stdin.readline())
is_used_1 = [False] * N
is_used_2 = [False] * (2 * N - 1)
is_used_3 = [False] * (2 * N - 1)
cnt = 0

def func(n):
    if n < N:
        for i in range(N):
            if not is_used_1[i] and not is_used_2[N - 1 + n - i] and not is_used_3[n + i]:
                is_used_1[i] = True
                is_used_2[N - 1 + n - i] = True
                is_used_3[n + i] = True
                func(n + 1)
                is_used_1[i] = False
                is_used_2[N - 1 + n - i] = False
                is_used_3[n + i] = False
    else:
        global cnt
        cnt += 1

func(0)
print(cnt)