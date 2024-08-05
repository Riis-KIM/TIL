T = 10

for test_case in range(1, T + 1):
    N = int(input())
    # 8*8
    arr = [input() for _ in range(8)]
    # 회문 개수
    count = 0
    ## 가로열 확인
    for item in arr:
        for j in range(8 - N + 1):
            dum = item[j:j + N]
            if dum == dum[::-1]:
                count += 1

    ## 세로열 확인
    for i in range(8):
        for j in range(8 - N + 1):
            dum = ''.join(arr[j + t][i] for t in range(N))
            if dum == dum[::-1]:
                count += 1

    print(f'#{test_case} {count}')
