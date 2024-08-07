def checkstack(stack, a):
    if not stack:
        return 0
    elif stack.pop() == a:
        return 1
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    str1 = input()

    # 스택, 짝이 맞는지 표시
    s = []
    for item in str1:
        # 괄호 시작할 경우 스택에 추가
        if item == '(' or item == '{' or item == '[':
            s.append(item)
        # 괄호 끝났을때 짝이 맞는지 확인
        elif item == ')' or item == '}' or item == ']':
            flg = checkstack(s, item)

    # 스택 비어있는지 확인
    if s:
        flg = 0

    print(f'#{test_case} {flg}')