# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수를 작성해보자
# 만약 합이 존재하면 1, 그렇지 않으면 0

import sys
sys.stdin = open('input.txt')

T = 3
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    n = len(arr)

def solve():

    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += arr[j]

        print(sum)
    print()

print(solve())