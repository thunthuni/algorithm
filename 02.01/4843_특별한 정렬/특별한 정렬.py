#큰 수 , 가장 작은 수 , 2번째 큰 수 , 2번째 작은 수
#번갈아서 정렬되는 것

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = [0] * N

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    max_idx = 0
    for max_i in range(N-1, N//2 - 1, -1):
        result[max_idx] = arr[max_i]
        max_idx += 2

    min_idx = 1
    for min_i in range(N//2):
        result[min_idx] = arr[min_i]
        min_idx += 2

    print(f'#{tc}', *result[:10])
