# 구하려고 하는 것 : 가장 많은 카드에 적힌 숫자 & 그 가장 많은 카드의 숫자
    # 카드 장수가 같을 때는! 적힌 숫자가 큰쪽 출력
# 어떻게 풀어보면 좋을까? 선택정렬을 사용하자
    # 데이터의 인덱스를 사용해서 counts 배열에 기록하자
    # counts 의 최대값을 찾아보자 => 장수가 가장 많은 것
        # 이 이후에 조건이 있게 된다.
            # 장수가 같은 카드가 있다면 카드에 적힌 숫자를 비교해서 큰 쪽을 출력한다
            # 없다면 장수에 적힌 숫자를 장수와 함께 프린트 한다.

    # 자 그럼 여기서! 카드에 적힌 숫자를 어떻게 알 수 있을까?
        # count의 인덱스와 카드에 적힌 숫자가 같다
# 입력
    # tc input
    # N = int(input())


import sys
sys.stdin = open('input.txt')

T = int(input())
K = 9
for tc in range(1, 51):
    N = int(input())
    card_num = list(map(int, input().split()))
    counts = [0] * (K + 1)

# 입력값 card_num 의 요소가 떨어져있지 않기 때문에 새로운 arr을 만들어서 할당해주자
# 그러기 위해서는 10으로 나눈 나머지 값을 할당해주고
# 다시 10으로 나눈 나머지값을 또 할당해주고 이거를 card_num의 길이만큼 반복해야 된다...?

arr = []
for x in card_num:
    arr.append(x % 10)

for x in card_num:
    counts[x] += 1

# max = counts[0]
# max.save = 0
# for idx in counts:
#     if counts[idx] > max:
#         max = counts[idx]

    # 여기서 value 는 최대값이 돼야 하고 / index 값또한 최대값이 돼야 한다
    # 그렇다면 조건문을 두개? 흠
    # 아 그러면 안되겠다 value가 최대값이 되는게 먼저니까
    # 그러면... value 최대값을 구한 후에...
    # 아나... 질문 잘못이해했네...?
    # 그니까 value 최대값 구하고 만약 카드 장수가 같을 때를 생각해서 역순으로 가면!!!!
    # 근데 역순 어케함... ㅎ


    # if value > maximum1:
    #     maximum1 = value
  ` max_list = []
    max_list.append(maximum1)
    i_max = 0
    for maximum1 in max_list:
        if len(max_list) == 1:
            print(count.index(maximum1), maximum1)
        if len(max_list) >= 1:
            for i_max in max_list:
                if count.index(i_max) > i_max:
                    i_max = count.index(i_max)
            print(count.index(i_max), i_max)
