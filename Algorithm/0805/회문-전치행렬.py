T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    # 회문 저장용
    ans = ''
    ## 가로열 확인
    for item in arr:
        for j in range(N-M+1):
            dum = item[j:j+M]
            if dum == dum[::-1]:
                ans = dum

    new_arr = [[0]*N for _ in range(N)]
    ## 전치행렬 이용해 중앙 기준으로 바꿈

    for i in range(N):
        for j in range(N):
            new_arr[i][j], new_arr[j][i] = arr[j][i], arr[i][j]

    for t in range(N):
        new_arr[t] = ''.join(new_arr[t])

    ## 처음 문자열 기준 세로 확인
    for item in new_arr:
        for j in range(N-M+1):
            dum = item[j:j+M]
            if dum == dum[::-1]:
                ans = dum

    print(f'#{test_case} {ans}')