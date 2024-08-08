T = int(input())

for test_case in range(1, T+1):
    # 문자 받아옴
    arr = list(map(str, input().split()))

    # 스택 생성
    stack = []
    # 연산자 확인용
    result = 'error'
    check = '+-*/'
    for item in arr:
        # . 일때 종료
        if item == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
            break
        # 숫자일 경우 스택에 추가
        elif item not in check:
            stack.append(int(item))
        # 연산자일 경우
        else:
            # 스택에 남아있는 숫자가 2개가 안될때 에러
            if len(stack) < 2:
                result = 'error'
                break
            # 사칙연산한 결과물 스택에 다시 추가
            else:
                a = stack.pop()
                b = stack.pop()
                if item == '+':
                    stack.append(a+b)
                elif item == '-':
                    stack.append(b-a)
                elif item == '*':
                    stack.append(a*b)
                elif item == '/':
                    stack.append(b//a)

    print(f'#{test_case} {result}')