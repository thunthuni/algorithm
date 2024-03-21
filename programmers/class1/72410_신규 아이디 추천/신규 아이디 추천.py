# 아이디의 길이 3자 이상 15자 이하
# 가능한 문자 타입: 알파벳 소문자, 숫자, -, _, .
    # . 는 처음과 끝에 X / 연속으로 사용 X

# 1) 대문자 -> 소문자
# 2) 사용 가능한 문자 타입 제외한 모든 문자 제거
# 3) . 2번 이상 연속된 부분을 하나로
# 4) . 이 처음이나 끝에 있다면 제거
# 5) 빈 문자열이라면 'a' 대입  V
# 6) if len(new_id) >= 16: new_id[:16] 를 제외한 나머지 모두 제거
    # 만약 제거후 . 가 끝에 위치한다면 제거
# 7) if len(new_id) <= 2: new_id[-1] 를 반복해서 끝에 붙임 until len(new_id) == 3

new_id = list(input())
# def solution(new_id):
my_lst = ['-', '_', '.']
def solution(id):
    if len(id) == 0 :
        id = id + 'a'
    if len(id) >= 16:
        new
    for word in id:

        # if not word.isalpha() and not word.isdecimal() and word not in my_lst:
        #     new_id.remove(word)
        #     print(id)
        # if word.isalpha() and word.isupper():
        #     word = word.lower()
        #     print(id)

    # if a == '.':
    #     if a
#     return id
solution(new_id)
