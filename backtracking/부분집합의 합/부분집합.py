
def f(k, n, s, M):
    global cnt
    if s == M:
        cnt += 1
        return
    elif n == k:
        return
    else:
        f(k+1, n, s+A[k], M)
        f(k+1, n, s, M)


A = list(map(int, input().split()))
cnt = 0
f(0, 10, 0, 0)
print(cnt)


