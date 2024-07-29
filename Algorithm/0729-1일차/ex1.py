T = int(input())

for test_case in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    max_num = num[0]
    min_num = num[0]
    for item in num:
        if item > max_num:
            max_num = item
        if item < min_num:
            min_num = item

    print(f'#{test_case + 1} {max_num - min_num}')
