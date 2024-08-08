T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = 0
    max_idx = 0

    for i in range(N):
        if arr[i] > max_num:
            max_num = arr[i]
            max_idx = i

    print(f'#{test_case} {max_idx+1} {max_num}')