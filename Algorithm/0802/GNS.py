T = int(input())

for test_case in range(1, T+1):

    dummy, length = input().split()
    arr = list(map(str, input().split()))

    # 다른 행성 숫자
    num_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 기존 문자열을 숫자로 변환
    for i in range(int(length)):
        for j in range(len(num_arr)):
            if arr[i] == num_arr[j]:
                arr[i] = j

    # 변환된 문자열을 정렬
    for i in range(int(length)-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 기존 문자열로 재변환
    for i in range(int(length)):
        for j in range(len(num_arr)):
            if arr[i] == j:
                arr[i] = num_arr[j]


    print(f'#{test_case}')
    print(*arr)
