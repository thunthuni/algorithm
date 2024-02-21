# N 개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

# 흠 어떻게 풀어야 할까


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N = 정수의 개수, M = 구간의 개수
    N, M = map(int, input().split()) # 어제 배운 언팩킹
    num_list = list(map(int, input().split()))

    # 일단 섹션을 구간의 개수에 따라서 나눠야겠당
    sums = []
    for i in range(len(num_list)):
        section = num_list[i: i + M]
        if len(section) != M: # 구간의 개수보다 적은 리스트들이 나오는것을 방지
            break

        sum = 0
        for num in section:
            sum += num
        sums.append(sum)

    min_v = sums[0] # 내장함수 혼란 방지
    max_v = sums[0]
    for value in sums:
        if value > max_v:
            max_v = value
        if value < min_v:
            min_v = valuee

    print(f'# {tc} {max_v - min_v}')