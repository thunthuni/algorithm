
N = list(map(int, input().split()))

# 직각삼각형의 정의: 가장 긴 변의 길이^2 = a^2 + b^2
# 먼저 가장 긴 길이를 찾는다
# 정의에 맞는지 반복문을 돌린다
# 맞다면 right 틀리면 wrong

# a, b, c로 인풋 받으면 더 낫긴 하겠다
# for i in range(3,1,-1):
#     for j in range(0,i):
#         if i[N]


max_v = 0
max_idx = 0
for i in range(len(N)):
    if max_v < N[i]:
        max_v = N[i]
        max_idx = i
N.pop(i)
if N[0]**2 + N[1]**2 == max_v**2:
    print('right')
else:
    print('wrong')
