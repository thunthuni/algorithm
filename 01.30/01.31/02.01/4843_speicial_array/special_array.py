# N개의 정수가 주어진다
# 가장 큰 수 <-> 가장 작은 수
# 2번째 큰 수 <-> 2번째 작은 수
    # 이런식으로 큰 수와 작은 수를 번갈아 정렬한것을 프린트

# 손으로 그려보았을 때, 가장 큰 숫자 절반이 짝수 인덱스로
    # 가장 작은 숫자 절반이 홀수 인덱스로 가더라

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    int_list = list(map(int, input().split()))
    count = [0] * N   # 비어있는 배열

# 먼저 오름차순으로 정렬하자
    def sort_list(int_list, N):
        for i in range(N-1, 0, -1):
            for j in range(0, i):
                if int_list[j] > int_list[j+1]:
                    int_list[j], int_list[j+1] = int_list[j+1], int_list[j]
        return int_list

    # 오름차순으로 정렬된 리스트
    result = sort_list(int_list, N)
    # result range(N/2) 이 count의 홀수 인덱스에 반복해서 들어간다
    #                range(N/2, -1)  역순으로 count의 짝수 인덱스에 반복해서 들어간다
    # 이해가 안가는 것
        # 어떻게 하면 정렬된 리스트의 값들이 count의 짝수 인덱스로 들어갈 수 있을까

    for idx in range(len(count)):
        for mini in result(0, N/2):
            if idx % 2 == 1:
                count[idx] = mini
        for maxi in result(N, N/2, -1):
            if idx % 2 == 0:
                count[idx] = maxi





