import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()
    open_br = ['(','{']
    close_br = [')', "}"]

    # 괄호들을 만난다면!
    count_op = 0
    count_cl = 0
    for idx in range(len(string)):
        for idx_op in range(1):
            if string[idx] == open_br[idx_op]:
                count_op += 1
        for idx_cl in range(1):
            if string[idx] == close_br[idx_cl]:
                count_cl += 1
    if count_op == count_cl:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

