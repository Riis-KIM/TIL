T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 경우의 수

    # 가로
    for i in range(N):      # 모든 행 조사
        cnt = 0             # 현재까지 연속한 1의 개수
        for j in range(N+1):
            if arr[i][j]:         # arr[i][j] == 1이면
                cnt+=1
            else:                   # 0이면
                if cnt == K:        # 길이가 K인 경우
                    ans += 1
                cnt = 0
    # 세로
    for i in range(N):      # 모든 행 조사
        cnt = 0             # 현재까지 연속한 1의 개수
        for j in range(N+1):
            if arr[j][i]:         # arr[i][j] == 1이면
                cnt+=1
            else:                   # 0이면
                if cnt == K:        # 길이가 K인 경우
                    ans += 1
                cnt = 0

    print(f'{test_case} {ans}')