import sys
sys.stdin = open('input.txt')

# 부분집합의 합이 0이 되는 것이 존재하는지?
# 존재하면 1 안하면 0

# k: 현재 호출에서 접근할 원소의 인덱스
# n: 배열의 크기
def f(k, n):
    global sum_v
    if n == k:  # b배열을 벗어나면
        for i in range(n):
            if b[i] == 1:
                sum_v += arr[i]
    else:
        b[k] = 0
        f(k + 1, n)
        b[k] = 1
        f(k + 1, n)

    return sum_v


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    sum_v = 0
    b = [0] * 10
    f(0, 10)

    if sum_v == 0:
        print(1)
    else:
        print(0)
