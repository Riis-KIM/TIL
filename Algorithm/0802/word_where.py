T = int(input())

for test_case in range(1, T+1):
    # N = 한 변의 길이 K = 글자 길이
    N, K = map(int, input().split())

    # 배열 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 들어갈 수 있는 자리 저장
    count = 0

    # 가로 탐색
    for i in range(N):
        j = 0
        flag = 0
        # 한줄 전체 확인
        while j < N:
            # 칸 색 별로 더함
            flag += arr[i][j]
            # 만약 K개의 칸이 나오고 다음 칸이 범위 내 일 경우
            if flag == K and j + 1 < N:
                mini = 0
                for m in range(K):
                    mini += arr[i][j-m]
                if arr[i][j+1] == 0 and mini == K:
                    count+=1
                    flag = 0
            # K개의 칸이 나오고 다음 칸이 범위 밖일 때
            elif flag == K and j+1 == N:
                mini = 0
                for m in range(K):
                    mini += arr[i][j-m]
                if mini == K:
                    count+=1
                    flag = 0
            j+=1

    # 세로 탐색
    for i in range(N):
        j = 0
        flag = 0
        # 한줄 전체 확인
        while j < N:
            # 칸 색 별로 더함
            flag += arr[j][i]
            # 만약 K개의 칸이 나오고 다음 칸이 범위 내 일 경우
            if flag == K and j + 1 < N:
                mini = 0
                for m in range(K):
                    mini += arr[j-m][i]
                if arr[j+1][i] == 0 and mini == K:
                    count+=1
                    flag = 0
            # K개의 칸이 나오고 다음 칸이 범위 밖일 때
            elif flag == K and j+1 == N:
                mini = 0
                for m in range(K):
                    mini += arr[j-m][i]
                if mini == K:
                    count+=1
                    flag = 0
            j+=1

    print(f'#{test_case} {count}')