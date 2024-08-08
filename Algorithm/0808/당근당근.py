T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    idx = 0
    min_sum = 99999
    for i in range(1, N):
        sum_a = 0
        sum_b = 0
        # 1번 일꾼이 수확한 당근 개수
        for j in range(i):
            sum_a += arr[j]

        # 2번 일꾼이 수확한 당근 개수
        for t in range(i, N):
            sum_b += arr[t]

        # 당근 차이 절대값 계산
        now_carrot = sum_a - sum_b
        if now_carrot < 0:
            now_carrot *= -1

        # 1번 일꾼의 당근 수와 2번 일꾼의 당근 수의 차이가 가장 작을 경우
        if now_carrot < min_sum:
            min_sum = now_carrot
            idx = i
    print(f'#{test_case} {idx} {min_sum}')

