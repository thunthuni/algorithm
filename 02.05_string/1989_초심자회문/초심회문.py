import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = str(input())
    temp = ''
    for idx in range(len(words)-1, -1,  -1): # 시작점, 끝값, 줄어드는양
        # [len(words):-1:-1] == [::-1]
        temp += words[idx]
        # 문자열을 더한다
    if temp == words:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

