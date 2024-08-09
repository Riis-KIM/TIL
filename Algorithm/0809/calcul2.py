T = 10
for test_case in range(1, T+1):
    N = int(input())
    infix = input()
    reverse = ''
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(N):
        if '1' <= infix[i] <='9':  # 피연산자인 경우
            reverse += infix[i]
        else:  # 연산자인 경우
            if top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                reverse += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:  # 남아있는 연산자를 수식뒤에 붙임
        reverse += stack[top]
        top -= 1

    # 후위 표기식으로 변환된 내용을 계산
    sum_stack = [0]*N
    top = -1
    for item in reverse:
        if '1' <= item <= '9':
            top += 1
            sum_stack[top] = int(item)
        else:
            a = sum_stack[top]
            top -= 1
            b = sum_stack[top]
            top -= 1
            if item == '+':
                top += 1
                sum_stack[top] = a + b
            elif item == '*':
                top += 1
                sum_stack[top] = a * b


    print(f'#{test_case} {sum_stack}')