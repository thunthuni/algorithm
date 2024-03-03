import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(str, range(1, N+1)))

# result = ''
# for num in arr:
#     if len(num) > 1:
#         if '3' not in num and '6' not in num and '9' not in num:
#             result += num
#         else:
#             for digit in num:
#                 if digit in '369':
#                     result += '-'
#                     continue
#                 else:
#                     continue
#     else:
#         if num in '369':
#             result += '-'
#         else:
#             result += num


for i in range(N):
    cnt = 0
    for num in arr[i]:
        if int(num) != 0 and int(num) % 3 == 0:
            cnt += 1
    if cnt > 0:
        arr[i] = '-'*cnt


print(*arr)