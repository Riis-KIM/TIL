# '(' 쇠막대기로 가정
# ')' 쇠막대기
# '()' 레이저 왼쪽글자가 '('
#
# total = 0
# cnt = 0
# for x in stick:
#     if x =='(':
#         cnt +=1
#     else: # ')'라면
#         # 이전꺼가 레이저면
#         # total += cnt
#         # 아니면...

for test_case in range(1, 1+T):

    for i in range(len(s)):
        if s[i]=='(':
            stick += 1
        elif s[i]==')' and s[i-1]=='(':
            cnt -= 1
            total += cnt
        else:
            total +=1
            cnt -=1