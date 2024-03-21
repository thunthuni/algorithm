import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = 8
    M = int(input())   # 찾아야 하는 회문의 길이
    letters = [input() for _ in range(N)]

# 문제를 제대로 읽자!!! 어제 자꾸 조건 하나씩 빼먹어서 몇번 엎었니^^....

# 8*8 글자판에서 제시된 길이를 가진 회문의 개수를 구하기
    count = 0
    for row in range(N):
        for idx in range(N):
            word = letters[row][idx: idx+M]
            temp = ''
            if len(word) == M:
                for index in range(M-1, -1, -1):
                    temp += word[index]
                if temp == word:
                    count += 1

    for col in range(N):
        col_list = []
        for row in range(N):
            col_list.append(letters[row][col])
        result1 = ''.join(col_list)


        for idx in range(N):
            result2 = result1[idx:idx+M]
            temp2 = ''
            if len(result2) == M:
                for col_idx in range(M-1, -1, -1):
                    temp2 += result2[col_idx]
                if temp2 == result2:
                    count += 1

    print(count)