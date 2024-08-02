T = int(input())

for test_case in range(1, T+1):
    # 정렬 범위
    N = int(input())
    # 정렬할 숫자
    arr = list(map(int, input().split()))

    for i in range(N):
        # 최대, 최소 찾기
        k = i
        max_idx = i
        min_idx = i
        while k < N:
            if arr[k] > arr[max_idx]:
                max_idx = k
            if arr[k] < arr[min_idx]:
                min_idx = k
            k += 1
        # 짝수에 큰값, 홀수에 작은값
        if i % 2 == 0:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f'#{test_case}', end=' ')
    print(*arr[:10])

