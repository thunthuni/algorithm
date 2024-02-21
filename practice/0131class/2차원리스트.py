#어떻게 입력하는가

import sys
sys.stdin =  open('../input.txt')

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(arr)

# 기본형태 [표현식 for _ in range(N)]
    # 임시 변수는 표현식 내부에서 사용 가능함
arr2 = [list(map(int, input().split())) for _ in range(N)] # -> [표현식, 표현식, list(map(int, input().split()))]
print(arr2)

