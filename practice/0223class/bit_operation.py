# N, M = list(map(int, input().split()))
#
# a = (bin(M))
#
# count = 0
# for num in str(a):
#     if num == '1':
#         count += 1
# if count == N:
#     print('ON')
# else:
#     print('OFF')
#
# M = 31
# N = 5
# def Test():
#     tar = M
#     for i in range(N):
#         if tar & 0x1 == 0:
#             return False
#         tar = tar >> 1
#     return True
# print(Test())

print(f'{0.1:.50f}')