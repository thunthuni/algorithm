import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    dump_num = int(input())
    box_h = list(map(int, input().split()))

# 최고점의 1을 최저점으로 1을 옮기면서 평탄화를 진행
# 주어진 덤프 횟수 동안 평탄화를 완료하면 최고점과 최저점의 높이 차를 반환
# 어떻게 풀면 될까?
# 먼저 가장 높은 박스를 반복해서 알아내야된다
    # 가장 낮은 박스도 똑같이
# 그리고 나서 가장 높은 박스 - 1 , 가장 낮은 박스 + 1
# 이거를 제한된 횟수( range(dum_num)) 만큼 진행시키면 되지 않을까...?
# 마지막으로 (가장 높은 박스의 높이 - 가장 낮은 박스의 높이) 를 반환하자

#









    # max_height = 0
    # min_height = 0
    #
    # for h in box_h:
    #     if h >= max_height :
    #         max_height = h
    #     if h <= min_height :
    #         min_height = h
    # # 여기까지 최대값과 최소값을 구했다
    # # 그 다음에는 최대값+1 ,최소값 -1 을 덤프 횟수동안 반복해야한다.
    #
    #         for max_height in range(dump_num):
    #             max_height -= 1
    #         for min_height in range(dump_num):
    #             min_height += 1
    #
    # print( max_height - min_height)