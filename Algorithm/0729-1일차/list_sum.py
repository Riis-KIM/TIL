T = int(input())

for test_case in range(1, T+1):
    M, N = map(int, input().split())
    arr = list(map(int, input().split()))

    max_num = sum(arr[0:N])
    min_num = sum(arr[0:N])
    for i in range(M-N+1):
        dummy = 0
        for j in range(N):
            dummy += arr[i+j]

        if dummy > max_num:
            max_num = dummy
        if dummy < min_num:
            min_num = dummy

    print(f'#{test_case} {max_num-min_num}')
