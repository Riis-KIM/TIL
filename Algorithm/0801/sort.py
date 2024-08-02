T = int(input())

for test_case in range(1, T+1):
    # 정렬 범위
    N = int(input())
    # 정렬할 숫자
    arr = list(map(int, input().split()))

    # # 거품정렬
    # for i in range(N-1, -1, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #
    # print(f'#{test_case}', end=' ')
    # print(*arr)

    # 선택정렬
    for i in range(N, 0, -1):
        max_idx = 0
        max_num = 0
        for j in range(i):
            if arr[j] > max_num:
                max_num = arr[j]
                max_idx = j
        arr[i-1], arr[max_idx] = arr[max_idx], arr[i-1]
    print(*arr)