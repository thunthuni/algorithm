import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    D = int(input())
    box_list = list(map(int, input().split()))

    # 할 일
    # 카운트 리스트를 사용하여 상자의 높이 별로 갯수를 등록
    # 등록된 카운트 리스트에서 최고점으로 쌓인 상자와, 최저점으로 쌓인 상자를 찾자!
    # 최고점 -1 /최저점 +1 (덤프 횟수만큼 반복)
    # 항상 최고점과 최저점의 값이 바뀔 수 있으므로 체크가 필수!

    count_list = [0] * 101 # 상자의 높이의 범위가 1 ~ 100 # 인덱스를 맞추기 위해 100 + 1
    # 초기 값은 가장 처음에 있는 값으로 설정
    max_height = box_list[0]
    min_height = box_list[0]

    for height in box_list:
        # box list의 height 는 count list의 index로 사용
        count_list[height] += 1

        # 가장 높은 높이, 낮은  높이를 구하자
        if max_height < height:
            max_height = height

        if min_height > height:
            min_height = height
    # 가장 높은 값, 낮은 값, count list 준비 완룟

    for _ in range(D):
        # 가장 높은 값에 -1
        # 가장 낮은 값에 +1
        count_list[max_height] -= 1
        count_list[max_height - 1] += 1

        count_list[min_height] -= 1
        count_list[min_height] += 1

        # 최대 최소 값이 존재하는지 계속해서 확인
        if count_list[max_height] == 0:
            max_height -= 1 # 최고 높이 갱신

        if count_list[min_height] == 0:
            min_height += 1 # 최저 높이 갱신

        if max_height - min_height <= 1:
            break


