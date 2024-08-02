T = int(input())

for test_case in range(1, T+1):
    # 정렬 범위
    N = int(input())
    # 정렬할 숫자
    arr = list(map(int, input().split()))

    # 정렬
    for i in range(N-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 큰값, 작은값 나눔
    med = int(N / 2)
    min_arr = arr[0:med]
    max_arr = arr[med:N]

    # 결과값 저장용 배열
    new_arr = [0 for _ in range(N)]

    # 최대값, 최소값을 알맞은 위치에 넣음
    for i in range(len(max_arr)):
        new_arr[i*2] = max_arr[len(max_arr) - i - 1]
    for i in range(len(min_arr)):
        new_arr[i*2+1] = min_arr[i]

    print(f'#{test_case}', end=' ')
    print(*new_arr[:10])