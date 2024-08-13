T = int(input())

for test_case in range(1, T+1):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈
    c1 = list(map(int, input().split()))

    pizza = -1
    queue = [0] * N
    pizza_idx = [0] * N
    # 피자 인덱스
    i = 0
    queue_idx = 0
    while True:
        if pizza >= 0:
            break
        queue[queue_idx] = queue[queue_idx]//2
        if queue[queue_idx] == 0 and i < M:
            queue[queue_idx] = c1[i]
            pizza_idx[queue_idx] = i + 1
            i += 1
        queue_idx = (queue_idx+1) % N

        if i == M and len([x for x in queue if x != 0]) == 1:
            for j in range(N):
                if queue[j] != 0:
                    pizza = j
                    break

    print(f'#{test_case} {pizza_idx[pizza]}')