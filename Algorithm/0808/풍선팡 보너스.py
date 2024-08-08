T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대값 저장
    max_count = 0
    # 모든 범위에서
    for i in range(N):
        for j in range(N):
            count = 0
            # 가로 길이 더함
            for p in range(N):
                count += arr[i][p]
            # 세로 길이 더함
            for q in range(N):
                count += arr[q][j]

            # 중간지점 2번 더해졌기 때문에 1번 빼줘야함
            count -= arr[i][j]
            if count > max_count:
                max_count = count

    print(f'#{test_case} {max_count}')