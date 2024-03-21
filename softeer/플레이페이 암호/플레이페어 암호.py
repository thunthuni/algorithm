import sys
sys.stdin = open('input.txt')


# 문제 정리
# I = J

# 1. 5 X 5 표에 문자열을 하나씩 넣는데
    # 알파벳이 반복되면 안된다
    # 표의 칸이 남는다면 아직 등장하지 않은 알파벳을 순서대로 채워놓는다
words = input()
arr = [[0]*5 for _ in range(5)]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = len(words)
#  words안에 있는 반복문자 제거하자
lst = [words[0]]

for i in range(1, N):
    if words[i] not in lst:
       lst.append(words[i])

n = len(lst)
i = 0

# 배열판에 넣자
# 남은 배열에는 사용하지 않은 알파벳들 차례대로 넣자
while i < n:
    for r in range(5):
        for c in range(5):
            arr[r][c] = lst[i]
            alphabets.remove(lst[i])
            i += 1
            # !list index out of range!
    # 남은 알파벳 넣으려고 하는 부분
    if i == n:

# 두 글자씩 나눠서 같은 알파벳이면
    # 두 글자 중간에 X 를 넣어주는데
    # 만약 XX 라면
        # X대신 Q를 넣어준다
# for i in range(0, N , 2)
    # if letter[i] == letter[i+1]:
        # if letter[i] != X:
            # 중간에 X넣기
        # else:
            # 중간에 Q넣기

