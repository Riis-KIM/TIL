T = int(input())

for test_case in range(1, T+1):

    # 해당 방법 사용 시 둘 다 필요없음
    dummy, dummy2 = input().split()

    # 주어진 문자열
    arr = list(map(str, input().split()))

    # 다른 행성 숫자, 비교용
    num_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    # 저장용 배열
    new_list = []

    # 주어진 문자열과 비교용 문자열을 서로 비교해서 같을 경우 저장용에 추가함
    for item in num_arr:
        for tem in arr:
            if item == tem:
                new_list.append(item)

    print(f'#{test_case}')
    print(*new_list)