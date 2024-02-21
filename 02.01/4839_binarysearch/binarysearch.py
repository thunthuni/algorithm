# A 와 B 가 있고 페이지 빨리 찾기 게임을 한다
# 책의 페이지 수는 정해져 있고 각자에게 찾아야하는 다른 페이지가 주어진다
# 이긴 사람을 출력하고 비긴경우에는 0을 출력한다

# 이진검색으로 차근차근 풀어보자

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력값이 한 줄에 전체 쪽수, A, B가 찾을 쪽수가 차례로 주어지는데 이것을 어떻게 입력하면 좋을까?
    # list 를 세로로 만들어줘야 될 것 같다
        # [400, 1000, 1000] , [300, 299, 222] ... 이런식으로
    # my_list = list(map(int, input().split()))
    # total_page = my_list[0]
    # a_page = my_list[1]
    # b_page = my_list[2]
    # 이렇게 해도 되긴 하지만 강사님께서 아래의 방법을 추천해주셨다
    total_page, a_page, b_page = map(int, input().split()) # 언팩킹

    def binary_search(total_page, target_page):
        count = 0
        start = 1
        end = total_page
        while start <= end:
            middle = (start + end)//2
            count += 1
            if middle == target_page:
                return count
            elif middle > target_page:
                end = middle - 1
            else:
                start = middle + 1
        return count



    result_a = binary_search(total_page, a_page)
    result_b = binary_search(total_page, b_page)

    # print(result_a, result_b)
    print(f'#{tc} ', end='')
    if result_a < result_b:
        print('A')
    if result_a > result_b:
        print('B')
    if result_a == result_b:
        print(0)
# A 와 B가 각 tc 에서 페이지를 찾을 수 있었는지 확인하는 함수를 생성했다
        # 이제는 각 함수가 True 이거나 False 이면 0 을 출력하고
        #        하나의 함수만 True를 출력한다면 그 함수에 해당하는 사람을 출력해야 한다

