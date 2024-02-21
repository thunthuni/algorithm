import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 글자의 길이 M = 회문의 길이
    string = [input() for _ in range(N)]

    # 일단 가로에서 회문 찾아볼까
    # 가로는 string[index]

    # for row in range(N):
    #     temp = ''
    #     for idx in range(M-1, -1, -1):
    #         temp += string[row][idx]
    #     if temp == string[row]:
    #         print(f'#{tc} {temp}')

    # 생긴 문제점: M 길이만큼 슬라이싱이 필요하다
    # 그럼 string[row][idx: idx+M]
    for row in range(N):
        for idx in range(N):
            word = string[row][idx: idx+M]
            temp = ''
            if len(word) == M:
                for index in range(M-1, -1, -1):
                    temp += word[index]
                if temp == word:
                    print(f'#{tc} {temp}')


    # 이제 세로를 찾아야 하는데 세로는 string[0][0] + string[1][0] + string[2][0] ....


    for col in range(N):
        col_list = []
        for row in range(N):
            col_list.append(string[row][col])
        result1 = ''.join(col_list)


        for idx in range(N):
            result2 = result1[idx:idx+M]
            temp2 = ''
            if len(result2) == M:
                for col_idx in range(M-1, -1, -1):
                    temp2 += result2[col_idx]
                if temp2 == result2:
                    print(f'#{tc} {temp2}')
