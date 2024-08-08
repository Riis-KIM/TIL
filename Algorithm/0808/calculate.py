T = 10
for test_case in range(1, T+1):
    N = int(input())

    str = input()

    # 연산자 저장용
    stack = []
    # 답 저장용
    ans = []

    # 후위 표기식으로 변환
    for item in str:
        if item.isdigit():
            ans.append(item)
        else:
            if not stack:
                stack.append(item)
            elif stack:
                ans.append(item)
    if stack:
        ans.append(stack.pop())

    # 후위 표기식으로 변환된 내용을 계산
    sum_stack = []
    for item in ans:
        if item.isdigit():
            sum_stack.append(int(item))
        else:
            a = sum_stack.pop()
            b = sum_stack.pop()
            sum_stack.append(a+b)

    print(f'#{test_case} {sum_stack.pop()}')