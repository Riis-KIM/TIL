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


    ## 세로열 확인
    for i in range(N):
        for j in range(N-M+1):
            dum = ''.join(arr[j+t][i] for t in range(M))
            if dum == dum[::-1]:
                ans = dum
    print(f'#{test_case} {ans}')
