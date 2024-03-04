dartResult = input()

integer = list(range(1, 10))
# bonus = {'S': a**1,'D': a**2, 'T': a**3, '*': a*2, '#': a*(-2)}

# def solution(dartResult):
stack = [dartResult[0]]
for idx in range(1, len(dartResult)):
    if dartResult[idx] not in integer:
        a = stack[idx - 1]
        bonus = {'S': int(a)**1, 'D': int(a)**2, 'T': int(a)**3, '*': int(a)*2, '#': int(a)*(-2)}
        stack.pop(-1)
        stack.append(bonus[idx])

    # answer = 0
    # return a
# for a in dartResult:
#     print(a)