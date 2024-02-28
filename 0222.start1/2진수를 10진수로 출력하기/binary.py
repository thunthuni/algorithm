import sys
sys.stdin = open('input.txt')

T = int(input())
N = int(input())
bi_lst = []
num_lst = []
for i in range(N):
    # for i in range()
    binary = list(map(int, input().strip()))
    bi_lst += binary    # 여러줄로 입력값을 줬지만 사실상 한 리스트에 들어가야 된ek
    # 7개씩 나눠서 새로운 리스트에 넣어준다
    # 궁금한것: 리스트 안에서 그대로 나눌 수 있나?

for idx in range(0, len(bi_lst), 7):
    new_lst = []
    new_lst.append(bi_lst[idx:idx+7])
    new_lst[0].reverse()
    num = 0
    for j in range(7):
        if new_lst[0][j] == 1:
            num += 2**j
        else:
            continue
    num_lst.append(num)
print(f'#1', *num_lst)





