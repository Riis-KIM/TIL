T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 사용 // 동 남 서 북
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    max_count = 0
    for i in range(N):
        for j in range(M):
            count = arr[i][j]
            length = arr[i][j]
            for item in delta:
                ni = i
                nj = j
                for _ in range(length):
                    ni += item[0]
                    nj += item[1]
                    if 0<=ni<N and 0<=nj<M:
                        count += arr[ni][nj]
            if max_count < count:
                max_count = count

    print(f'#{test_case} {max_count}')