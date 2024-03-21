import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    N, lst = input().split()
    lst = list(lst)
    i = 0
    length = int(N)
    while i + 1 < length:
        if lst[i] == lst[i+1]:
            # pop(index) 복잡합
            lst.pop(i)
            lst.pop(i)
            i -= 1
            length -= 2
        else:
            i += 1
    print(f'#{tc}', ''.join(lst))
    # 원본 배열은 수정하지 않음
    # 스택 이용하기